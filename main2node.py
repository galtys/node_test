import py_support
_idrisworld=None
undefined=None
def BigInt(x):
  return x

Prelude_Types_fastUnpack = ( lambda x:py_support.fastUnpack((x)))
Prelude_IO_prim__putStr = ( lambda x,world:print(x,end=''))
def x24tcOpt_1(SS0): 
  if(False): 
    pass;
  elif (SS0.get('a1')==0):  
    if(False): 
      pass;
    elif (SS0.get('a2').get('h_x')==undefined):  
      return {'h_x': 0, 'a1': {'a1': SS0.get('a2').get('a1')}}
    else: 
      return {'h_x': 0, 'a1': {'h_x': 0}}
    
  else: 
    SS8 = (SS0.get('a1')-1)
    if(False): 
      pass;
    elif (SS0.get('a2').get('h_x')==undefined):  
      return {'h_x': 1, 'a1': SS8, 'a2': SS0.get('a2').get('a2')}
    else: 
      return {'h_x': 0, 'a1': {'h_x': 0}}
    
  


def Prelude_Types_getAt(SS0, SS1): 
  return __tailRec(x24tcOpt_1, {'h_x': 1, 'a1': SS0, 'a2': SS1})


def __mainExpression_0(): 
  return PrimIO_unsafePerformIO(Main2node_main())


def prim__add_Integer(SS0, SS1): 
  return (SS0+SS1)


def prim__sub_Integer(SS0, SS1): 
  return (SS0-SS1)


def prim__mul_Integer(SS0, SS1): 
  return (SS0*SS1)


def Main2node_test(SS0): 
  return Prelude_Cast_cast_Cast_Integer_String((SS0+10))


def Main2node_main(): 
  SSf = lambda b :lambda a :lambda SS10 :lambda SS11 :lambda SS12 :__local_fun2(b,a,SS10,SS11,SS12)
  def __local_fun2(b, a, SS10, SS11, SS12): 
    SS13 = SS10(SS12)
    SS16 = SS11(SS12)
    return SS13(SS16)
  
  SS4 = {'a1': lambda b :lambda a :lambda func :lambda SS6 :lambda SS7 :Prelude_IO_map_Functor_IO(func, SS6, SS7), 'a2': lambda a :lambda SSd :lambda SSe :SSd, 'a3': SSf}
  SS1b = lambda b :lambda a :lambda SS1c :lambda SS1d :lambda SS1e :__local_fun3(b,a,SS1c,SS1d,SS1e)
  def __local_fun3(b, a, SS1c, SS1d, SS1e): 
    SS1f = SS1c(SS1e)
    return SS1d(SS1f)(SS1e)
  
  SS26 = lambda a :lambda SS27 :lambda SS28 :__local_fun4(a,SS27,SS28)
  def __local_fun4(a, SS27, SS28): 
    SS29 = SS27(SS28)
    return SS29(SS28)
  
  SS3 = {'a1': SS4, 'a2': SS1b, 'a3': SS26}
  SS2 = {'a1': SS3, 'a2': lambda a :lambda SS2f :SS2f}
  SS1 = {'a1': SS2, 'a2': {'a1': lambda x :Prelude_Show_show_Show_String(x), 'a2': lambda d :lambda x :Prelude_Show_showPrec_Show_String(d, x)}}
  return Prelude_IO_printLn(SS1, Main2node_test(23))


def Builtin_snd(SS0): 
  return SS0.get('a2')


def Builtin_fst(SS0): 
  return SS0.get('a1')


def Builtin_believe_me(SS0): 
  return SS0


def Prelude_Types_prim__integerToNat(SS0): 
  SS1=None
  if(False): 
    pass;
  elif (((0<=SS0))==0):  
    SS1 = 0
  else: 
    SS1 = 1
  
  if(False): 
    pass;
  elif (SS1==1):  
    return Builtin_believe_me(SS0)
  
  elif (SS1==0):  
    return 0
  else: 
    pass;
  


def Prelude_Types_isDigit(SS0): 
  if(False): 
    pass;
  elif (Prelude_EqOrd_x3ex3d_Ord_Char(SS0, '0')==1):  
    return Prelude_EqOrd_x3cx3d_Ord_Char(SS0, '9')
  
  elif (Prelude_EqOrd_x3ex3d_Ord_Char(SS0, '0')==0):  
    return 0
  else: 
    pass;
  


def Prelude_EqOrd_compare_Ord_Integer(SS0, SS1): 
  if(False): 
    pass;
  elif (Prelude_EqOrd_x3c_Ord_Integer(SS0, SS1)==1):  
    return 0
  
  elif (Prelude_EqOrd_x3c_Ord_Integer(SS0, SS1)==0):  
    if(False): 
      pass;
    elif (Prelude_EqOrd_x3dx3d_Eq_Integer(SS0, SS1)==1):  
      return 1
    
    elif (Prelude_EqOrd_x3dx3d_Eq_Integer(SS0, SS1)==0):  
      return 2
    else: 
      pass;
    
  else: 
    pass;
  


def Prelude_EqOrd_x3e_Ord_Char(SS0, SS1): 
  if(False): 
    pass;
  elif (((SS0>SS1))==0):  
    return 0
  else: 
    return 1
  


def Prelude_EqOrd_x3ex3d_Ord_Char(SS0, SS1): 
  if(False): 
    pass;
  elif (((SS0>=SS1))==0):  
    return 0
  else: 
    return 1
  


def Prelude_EqOrd_x3dx3d_Eq_Ordering(SS0, SS1): 
  if(False): 
    pass;
  elif (SS0==0):  
    if(False): 
      pass;
    elif (SS1==0):  
      return 1
    else: 
      return 0
    
  
  elif (SS0==1):  
    if(False): 
      pass;
    elif (SS1==1):  
      return 1
    else: 
      return 0
    
  
  elif (SS0==2):  
    if(False): 
      pass;
    elif (SS1==2):  
      return 1
    else: 
      return 0
    
  else: 
    return 0
  


def Prelude_EqOrd_x3dx3d_Eq_Integer(SS0, SS1): 
  if(False): 
    pass;
  elif (((SS0==SS1))==0):  
    return 0
  else: 
    return 1
  


def Prelude_EqOrd_x3dx3d_Eq_Char(SS0, SS1): 
  if(False): 
    pass;
  elif (((SS0==SS1))==0):  
    return 0
  else: 
    return 1
  


def Prelude_EqOrd_x3c_Ord_Integer(SS0, SS1): 
  if(False): 
    pass;
  elif (((SS0<SS1))==0):  
    return 0
  else: 
    return 1
  


def Prelude_EqOrd_x3cx3d_Ord_Char(SS0, SS1): 
  if(False): 
    pass;
  elif (((SS0<=SS1))==0):  
    return 0
  else: 
    return 1
  


def Prelude_EqOrd_x2fx3d_Eq_Ordering(SS0, SS1): 
  if(False): 
    pass;
  elif (Prelude_EqOrd_x3dx3d_Eq_Ordering(SS0, SS1)==1):  
    return 0
  
  elif (Prelude_EqOrd_x3dx3d_Eq_Ordering(SS0, SS1)==0):  
    return 1
  else: 
    pass;
  


def Prelude_Show_n__2390_10841_asciiTab(SS0): 
  return {'a1': 'NUL', 'a2': {'a1': 'SOH', 'a2': {'a1': 'STX', 'a2': {'a1': 'ETX', 'a2': {'a1': 'EOT', 'a2': {'a1': 'ENQ', 'a2': {'a1': 'ACK', 'a2': {'a1': 'BEL', 'a2': {'a1': 'BS', 'a2': {'a1': 'HT', 'a2': {'a1': 'LF', 'a2': {'a1': 'VT', 'a2': {'a1': 'FF', 'a2': {'a1': 'CR', 'a2': {'a1': 'SO', 'a2': {'a1': 'SI', 'a2': {'a1': 'DLE', 'a2': {'a1': 'DC1', 'a2': {'a1': 'DC2', 'a2': {'a1': 'DC3', 'a2': {'a1': 'DC4', 'a2': {'a1': 'NAK', 'a2': {'a1': 'SYN', 'a2': {'a1': 'ETB', 'a2': {'a1': 'CAN', 'a2': {'a1': 'EM', 'a2': {'a1': 'SUB', 'a2': {'a1': 'ESC', 'a2': {'a1': 'FS', 'a2': {'a1': 'GS', 'a2': {'a1': 'RS', 'a2': {'a1': 'US', 'a2': {'h_x': 0}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}


def Prelude_Show_show_Show_String(SS0): 
  return ('\"'+Prelude_Show_showLitString(Prelude_Types_fastUnpack(SS0), '\"'))


def Prelude_Show_show_Show_Int(SS0): 
  return Prelude_Show_showPrec_Show_Int({'h_x': 0}, SS0)


def Prelude_Show_showPrec_Show_String(SS0, SS1): 
  return Prelude_Show_show_Show_String(SS1)


def Prelude_Show_showPrec_Show_Int(SS0, SS1): 
  return Prelude_Show_primNumShow(lambda SS4 :str(SS4), SS0, SS1)


def Prelude_Show_compare_Ord_Prec(SS0, SS1): 
  if(False): 
    pass;
  elif (SS0.get('h_x')==4):  
    if(False): 
      pass;
    elif (SS1.get('h_x')==4):  
      return Prelude_EqOrd_compare_Ord_Integer(SS0.get('a1'), SS1.get('a1'))
    else: 
      return Prelude_EqOrd_compare_Ord_Integer(Prelude_Show_precCon(SS0), Prelude_Show_precCon(SS1))
    
  else: 
    return Prelude_EqOrd_compare_Ord_Integer(Prelude_Show_precCon(SS0), Prelude_Show_precCon(SS1))
  


def Prelude_Show_x3ex3d_Ord_Prec(SS0, SS1): 
  return Prelude_EqOrd_x2fx3d_Eq_Ordering(Prelude_Show_compare_Ord_Prec(SS0, SS1), 0)


def Prelude_Show_showParens(SS0, SS1): 
  if(False): 
    pass;
  elif (SS0==0):  
    return SS1
  
  elif (SS0==1):  
    return ('('+(SS1+')'))
  else: 
    pass;
  


def Prelude_Show_showLitString(SS0, SS1): 
  if(False): 
    pass;
  elif (SS0.get('h_x')==0):  
    return SS1
  
  elif (SS0.get('h_x')==undefined):  
    if(False): 
      pass;
    elif (SS0.get('a1')=='\"'):  
      return ('test_as_hex\"'+Prelude_Show_showLitString(SS0.get('a2'), SS1))
    else: 
      return Prelude_Show_showLitChar(SS0.get('a1'))(Prelude_Show_showLitString(SS0.get('a2'), SS1))
    
  else: 
    pass;
  


def Prelude_Show_showLitChar(SS0):
  return (lambda SS2 :(SS0+SS2))
  if(False): 
    pass;
  elif (SS0=='test_as_hex'):  
    return lambda SS2 :('test_as_hexa'+SS2)
  
  elif (SS0=='test_as_hex'):  
    return lambda SS5 :('test_as_hexb'+SS5)
  
  elif (SS0=='test_as_hex'):  
    return lambda SS8 :('test_as_hexf'+SS8)
  
  elif (SS0=='\n'):  
    return lambda SSb :('test_as_hexn'+SSb)
  
  elif (SS0=='\r'):  
    return lambda SSe :('test_as_hexr'+SSe)
  
  elif (SS0=='test_as_hex'):  
    return lambda SS11 :('test_as_hext'+SS11)
  
  elif (SS0=='test_as_hex'):  
    return lambda SS14 :('test_as_hexv'+SS14)
  
  elif (SS0=='test_as_hex'):  
    return lambda SS17 :Prelude_Show_protectEsc(lambda SS1a :Prelude_EqOrd_x3dx3d_Eq_Char(SS1a, 'H'), 'test_as_hexSO', SS17)
  
  elif (SS0=='test_as_hex'):  
    return lambda SS20 :('test_as_hexDEL'+SS20)
  
  elif (SS0=='test_as_hex'):  
    return lambda SS23 :('test_as_hextest_as_hex'+SS23)
  else: 

    def __local_fun11(SS26): 
      SS27 = Prelude_Types_getAt(Prelude_Types_prim__integerToNat(BigInt( str(SS0[0]) )), Prelude_Show_n__2390_10841_asciiTab(SS0))
      if(False): 
        pass;
      elif (SS27.get('h_x')==undefined):  
        return ('test_as_hex'+(SS27.get('a1')+SS26))
      
      elif (SS27.get('h_x')==0):  
        if(False): 
          pass;
        elif (Prelude_EqOrd_x3e_Ord_Char(SS0, 'test_as_hex')==1):  
          return ('test_as_hex'+Prelude_Show_protectEsc(lambda SS3c :Prelude_Types_isDigit(SS3c), Prelude_Show_show_Show_Int(_truncInt32(SS0.codePointAt(0))), SS26))
        
        elif (Prelude_EqOrd_x3e_Ord_Char(SS0, 'test_as_hex')==0):  
          return (SS0+SS26)
        else: 
          pass;
        
      else: 
        pass;
    return lambda SS26 :__local_fun11(SS26)  
    
  


def Prelude_Show_protectEsc(SS0, SS1, SS2): 
  SS5=None
  if(False): 
    pass;
  elif (Prelude_Show_firstCharIs(SS0, SS2)==1):  
    SS5 = 'test_as_hex&'
  
  elif (Prelude_Show_firstCharIs(SS0, SS2)==0):  
    SS5 = ''
  else: 
    pass;
  
  SS4 = (SS5+SS2)
  return (SS1+SS4)


def Prelude_Show_primNumShow(SS0, SS1, SS2): 
  SS3 = SS0(SS2)
  SS7=None
  if(False): 
    pass;
  elif (Prelude_Show_x3ex3d_Ord_Prec(SS1, {'h_x': 5})==1):  
    SS7 = Prelude_Show_firstCharIs(lambda SSe :Prelude_EqOrd_x3dx3d_Eq_Char(SSe, '-'), SS3)
  
  elif (Prelude_Show_x3ex3d_Ord_Prec(SS1, {'h_x': 5})==0):  
    SS7 = 0
  else: 
    pass;
  
  return Prelude_Show_showParens(SS7, SS3)


def Prelude_Show_precCon(SS0): 
  if(False): 
    pass;
  elif (SS0.get('h_x')==0):  
    return 0
  
  elif (SS0.get('h_x')==1):  
    return 1
  
  elif (SS0.get('h_x')==2):  
    return 2
  
  elif (SS0.get('h_x')==3):  
    return 3
  
  elif (SS0.get('h_x')==4):  
    return 4
  
  elif (SS0.get('h_x')==5):  
    return 5
  
  elif (SS0.get('h_x')==6):  
    return 6
  else: 
    pass;
  


def Prelude_Show_firstCharIs(SS0, SS1): 
  if(False): 
    pass;
  elif (SS1==''):  
    return 0
  else: 
    return SS0((SS1.charAt(0)))
  


def Prelude_IO_map_Functor_IO(SS0, SS1, SS2): 
  SS3 = SS1(SS2)
  return SS0(SS3)


def Prelude_IO_putStrLn(SS0, SS1): 
  return Prelude_IO_putStr(SS0, (SS1+'\n'))


def Prelude_IO_putStr(SS0, SS1): 
  return SS0.get('a2')(py_support.erased)(lambda SS7 :Prelude_IO_prim__putStr(SS1, SS7))


def Prelude_IO_printLn(SS0, SS1): 
  SS7 = Builtin_snd(SS0)
  SS6 = SS7.get('a1')(SS1)
  return Prelude_IO_putStrLn(Builtin_fst(SS0), SS6)


def PrimIO_unsafePerformIO(SS0): 
  return PrimIO_unsafeCreateWorld(lambda w :SS0(w))


def PrimIO_unsafeCreateWorld(SS0): 
  return SS0(_idrisworld)


def Prelude_Cast_cast_Cast_Integer_String(SS0): 
  return str(SS0)



__mainExpression_0()
