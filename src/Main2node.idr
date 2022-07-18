module Main2node

import Prelude

--%foreign "node:lambda: x => console.log(x)"
--prim__consoleLog : String -> PrimIO ()

consoleLog : HasIO io => String -> io ()
consoleLog x = putStrLn x


data Ocas = Bud | Nebo Int String | Muf4 | K4a | UIda4 String

data Ocas2 = Kuk Int | Muf Double | Nic

notId : {a : Type} -> a -> a
notId {a=Int} x = x + 1
notId {a=Ocas2} x = Nic
notId x = x

show_ocas2 : Ocas2 -> String
show_ocas2 (Kuk x) = (show x)++("kuk")
show_ocas2 (Muf x) = "double: " ++(show x)
show_ocas2 Nic = "nic"

show_ocas : Ocas -> String
show_ocas Bud = "Bud Hello World"
show_ocas (Nebo x u) = "Nebo"++(show x)++u
show_ocas Muf4 = "4sa"
show_ocas K4a = "das"
show_ocas (UIda4 a) = a


show_list : (List Int) -> Int
show_list [] = 0
show_list [x] = 5
show_list (x::xs) = x + (show_list xs)

const_nebo : String->Ocas
const_nebo muf = Nebo 12 muf

x:Nat
x=1099956644355

y:Nat
y= notId (x+1)


test : Integer -> String
test = cast . (+ 10)

main : IO ()
main = do     
     {-
     putStrLn $ test 23
     putStrLn $ show 23
     putStrLn $ show_ocas Bud
     putStrLn $ show_ocas Bud
     
     putStrLn $ show_ocas $ const_nebo "muf"
     putStrLn $ show_ocas2 $ Nic
     putStrLn $ show $show_list [4,9,2,9]
     putStrLn $  cast (x)
     putStrLn "Hello World"
     -}
     putStrLn $ show "Hello World"
--main : IO ()
--main = do
  --putStrLn "Hello World"
--  orig_test
