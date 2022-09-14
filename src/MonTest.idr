module MonTest

import Control.Monad.State
import Data.MSF
import Data.MSF.Trans
import Generics.Derive

%language ElabReflection
%default total

interface Monad m => MonadUI m where
  disableInc   : Bool -> m ()
  disableDec   : Bool -> m ()
  disableReset : Bool -> m ()
  dispCount    : Int8 -> m ()

Ev : Type
Ev = Int8 -> Int8

msf : MonadUI m => MSF m Ev ()
msf = accumulateWith apply 0 >>>
      fan_ [ arrM dispCount
           , (>= 10)    ^>> arrM disableInc
           , (<= (-10)) ^>> arrM disableDec
           , (== 0)     ^>> arrM disableReset
           ]

record UI where
  constructor MkUI
  inc   : Bool
  dec   : Bool
  reset : Bool
  out   : String

ini : UI
ini = MkUI True True True ""

%runElab derive "UI" [Generic,Meta,Eq,Show]

MonadUI (State UI) where
  disableInc   b = modify { inc := not b }
  disableDec   b = modify { dec := not b }
  disableReset b = modify { reset := not b }
  dispCount    n = modify { out := #"Count: \#{show n}"# }

data Input = Inc | Dec | Reset

%runElab derive "Input" [Generic,Meta,Eq,Show]

onInput : MSF (State UI) Input (NS I [Ev,Input])
onInput = fan [get, id] >>> bool valid >>> choice [arr toFun, snd]
  where valid : NP I [UI,Input] -> Bool
        valid [ui,Inc]   = ui.inc
        valid [ui,Dec]   = ui.dec
        valid [ui,Reset] = ui.reset

        toFun : NP I [UI,Input] -> Int8 -> Int8
        toFun [_,Inc  ] = (+  1)
        toFun [_,Dec  ] = (+ -1)
        toFun [_,Reset] = const 0

simulate : List Input -> List String
simulate evs = evalState ini . embed evs
             $ onInput >>> collect
                 [ msf >>> get >>^ show
                 , arr $ \i => "Ignored invalid input: \{show i}"
                 ]

testUI : List String
testUI = simulate $  replicate 11 Inc
                  ++ replicate 2 Reset
                  ++ replicate 11 Dec

--import Docs.UIEx1
kocour : String
kocour = " A kocour"
main : IO ()
main = putStrLn $ show testUI
