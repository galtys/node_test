erased=None
_idrisworld=None #?symbol?
def fastUnpack(x):
    acc = {'h_x':0}
    for i in x:
        acc = {'a1':i, 'a2':acc}
    return acc

def __lazy(thunk):
    res=None
    def f():
        if thunk is undefined:
            return res
        res=thunk()
        thunk=undefined
        return res
    return f


def __prim_js2idris_aray(x):
    acc={'h_x':0}
    for i in x:
        acc = {'a1':i, a2:acc}
    return acc

def __prim_idris2js_array(x):
    result=[]
    while x.get('h_x') is undefined:
        result.append( x['a1'] )
        x = x['a2']
    return result
#?
def __prim_stringIteratorNew(_str):
    return 0
def __prim_stringIteratorToString(x, str_, it, f):
  return f(str.slice(it))
def __prim_stringIteratorNext(str, it):
    pass #?
#?

def _crashExp(x):
    raise (ValueError x)

def _bigIntOfString(s):
    return long(s)

def _numberOfString(s):
    return int(s)

import math

_intOfString = lambda s: math.trunc(_numberOfString(s))


def _truncToChar(x):
    if (x >= 0 and x <= 55295) or (x >= 57344 and x <= 1114111):
        return chr(x)
    else:
        return chr(0)
        
def _truncInt8(x):
    res = x & 0xff
    if (res >= 0x80):
        return res - 0x100
    else:
        return res

_truncBigInt8=_truncInt8

def _div(a,b):
    q=math.trunc(1.0*a/b)
    r=a%b
    # r < 0 ? (b > 0 ? q - 1 : q + 1) : q
    if r<0:
        if b>0:
            return q-1
        else:
            return q+1
    else:
        return q
_divBigInt=_div

def _mod(a,b):
    r = a%b
    if r<0:
        if b>0:
            return r+b
        else:
            return r-b
    else:
        return r

_modBigInt=_mod

_add8s = lambda a,b: _truncInt8(a+b)
_sub8s = lambda a,b: _truncInt8(a-b)
_mul8s = lambda a,b: _truncInt8(a*b)
_div8s = lambda a,b: _truncInt8( _div(a,b) )
_shl8s = lambda a,b: _truncInt8(a<<b)
_shr8s = lambda a,b: _truncInt8(a>>b)

def _truncInt16(x):
    res = x & 0xffff
    if (res>=0x8000):
        return res-0x10000
    else:
        return res
_truncBigInt16 = _truncInt16

_add16s = lambda a,b: _truncInt16(a+b)
_sub16s = lambda a,b: _truncInt16(a-b)
_mul16s = lambda a,b: _truncInt16(a*b)
_div16s = lambda a,b: _truncInt16( _div(a,b) )
_shl16s = lambda a,b: _truncInt16(a<<b)
_shr16s = lambda a,b: _truncInt16(a>>b)

_truncInt32 = lambda x: x&0xffffffff

_truncBigInt32=_truncInt32

_add32s = lambda a,b: _truncInt32(a+b)
_sub32s = lambda a,b: _truncInt32(a-b)
_mul32s = lambda a,b: _truncInt32(a*b)  #todo?
_div32s = lambda a,b: _truncInt32( _div(a,b) )
_shl32s = lambda a,b: _truncInt32(a<<b)
_shr32s = lambda a,b: _truncInt32(a>>b)

def _truncBigInt64(x):
  res = x & 0xffffffffffffffffn;
  if (res >= 0x8000000000000000):
      return (res - 0x10000000000000000)
  else:
      return res

_add64s = lambda a,b: _truncInt64(a+b)
_sub64s = lambda a,b: _truncInt64(a-b)
_mul64s = lambda a,b: _truncInt64(a*b)  #todo?
_div64s = lambda a,b: _truncInt64( _divBigInt(a,b) )
_shl64s = lambda a,b: _truncInt64(a<<b)
_shr64s = lambda a,b: _truncInt64(a>>b)

#Bits8
def _truncUInt8(x):
    return (x & 0xff)
_truncUBigInt8 = _truncUInt8

_add8u = lambda a,b: (a+b) & 0xff
_sub8u = lambda a,b: (a-b) & 0xff
_mul8u = lambda a,b: (a*b) & 0xff
_div8u = lambda a,b: math.trunc(a/b)
_shl8u = lambda a,b: (a<<b) & 0xff
_shr8u = lambda a,b: (a>>b) & 0xff

_truncUInt16 = lambda x: x&0xffff
_truncUBigInt16=_truncUInt16

_add16u = lambda a,b: (a+b) & 0xffff
_sub16u = lambda a,b: (a-b) & 0xffff
_mul16u = lambda a,b: (a*b) & 0xffff
_div16u = lambda a,b: math.trunc(a/b)
_shl16u = lambda a,b: (a<<b) & 0xffff
_shr16u = lambda a,b: (a>>b) & 0xffff

_truncUInt32 = lambda x: x&0xffffffff
_truncUBigInt32=_truncUInt32

_add32u = lambda a,b: _truncUInt32(a+b)
_sub32u = lambda a,b: _truncUInt32(a-b)
_mul32u = lambda a,b: _truncUInt32(a*b)  #todo?
_div32u = lambda a,b: _truncUInt32( _mul32s(a,b) )
_shl32u = lambda a,b: _truncUInt32(a<<b)
_shr32u = lambda a,b: _truncUInt32(a>>b)

_and32u = lambda a,b: _truncUInt32(a&b)
_or32u = lambda a,b: _truncUInt32(a|b)
_xor32u = lambda a,b: _truncUInt32(a&b) #???

_truncUInt64 = lambda x: x&0xffffffffffffffff
_truncUBigInt64=_truncUInt64

_add64u = lambda a,b: (a+b) & 0xffffffffffffffff
_sub64u = lambda a,b: (a-b) & 0xffffffffffffffff
_mul64u = lambda a,b: (a*b) & 0xffffffffffffffff
_div64u = lambda a,b: (a/b)
_shl64u = lambda a,b: (a<<b) & 0xffffffffffffffff
_shr64u = lambda a,b: (a>>b) & 0xffffffffffffffff

_strReverse = lambda x : x[::-1]
_substr = lambda o,l,x : x.slice(o,o+l)

