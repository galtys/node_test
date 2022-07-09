class IdrisError extends Error { }

function __prim_js2idris_array(x){
  if(x.length === 0){
    return {h:0}
  } else {
    return {a1:x[0],a2: __prim_js2idris_array(x.slice(1))}
  }
}

function __prim_idris2js_array(x){
  const result = Array();
  while (x.h === undefined) {
    result.push(x.a1); x = x.a2;
  }
  return result;
}

function __lazy(thunk) {
  let res;
  return function () {
    if (thunk === undefined) return res;
    res = thunk();
    thunk = undefined;
    return res;
  };
};

function __prim_stringIteratorNew(str) {
  return 0
}

function __prim_stringIteratorToString(_, str, it, f) {
  return f(str.slice(it))
}

function __prim_stringIteratorNext(str, it) {
  if (it >= str.length)
    return {h: 0};
  else
    return {a1: str.charAt(it), a2: it + 1};
}

function __tailRec(f,ini) {
  let obj = ini;
  while(true){
    switch(obj.h){
      case 0: return obj.a1;
      default: obj = f(obj);
    }
  }
}

const _idrisworld = Symbol('idrisworld')

const _crashExp = x=>{throw new IdrisError(x)}

const _bigIntOfString = s=> {
  try {
    const idx = s.indexOf('.')
    return idx === -1 ? BigInt(s) : BigInt(s.slice(0, idx))
  } catch (e) { return 0n }
}

const _numberOfString = s=> {
  try {
    const res = Number(s);
    return isNaN(res) ? 0 : res;
  } catch (e) { return 0 }
}

const _intOfString = s=> Math.trunc(_numberOfString(s))

const _truncToChar = x=> String.fromCodePoint(
  (x >= 0 && x <= 55295) || (x >= 57344 && x <= 1114111) ? x : 0
)

// Int8
const _truncInt8 = x => {
  const res = x & 0xff;
  return res >= 0x80 ? res - 0x100 : res;
}

const _truncBigInt8 = x => {
  const res = Number(x & 0xffn);
  return res >= 0x80 ? res - 0x100 : res;
}

const _add8s = (a,b) => _truncInt8(a + b)
const _sub8s = (a,b) => _truncInt8(a - b)
const _mul8s = (a,b) => _truncInt8(a * b)
const _div8s = (a,b) => _truncInt8(Math.trunc(a / b))
const _shl8s = (a,b) => _truncInt8(a << b)
const _shr8s = (a,b) => _truncInt8(a >> b)

// Int16
const _truncInt16 = x => {
  const res = x & 0xffff;
  return res >= 0x8000 ? res - 0x10000 : res;
}

const _truncBigInt16 = x => {
  const res = Number(x & 0xffffn);
  return res >= 0x8000 ? res - 0x10000 : res;
}

const _add16s = (a,b) => _truncInt16(a + b)
const _sub16s = (a,b) => _truncInt16(a - b)
const _mul16s = (a,b) => _truncInt16(a * b)
const _div16s = (a,b) => _truncInt16(Math.trunc(a / b))
const _shl16s = (a,b) => _truncInt16(a << b)
const _shr16s = (a,b) => _truncInt16(a >> b)

//Int32
const _truncInt32 = x => x & 0xffffffff

const _truncBigInt32 = x => {
  const res = Number(x & 0xffffffffn);
  return res >= 0x80000000 ? res - 0x100000000 : res;
}

const _add32s = (a,b) => _truncInt32(a + b)
const _sub32s = (a,b) => _truncInt32(a - b)
const _div32s = (a,b) => _truncInt32(Math.trunc(a / b))

const _mul32s = (a,b) => {
  const res = a * b;
  if (res <= Number.MIN_SAFE_INTEGER || res >= Number.MAX_SAFE_INTEGER) {
    return _truncInt32((a & 0xffff) * b + (b & 0xffff) * (a & 0xffff0000))
  } else {
    return _truncInt32(res)
  }
}

//Int64
const _truncBigInt64 = x => {
  const res = x & 0xffffffffffffffffn;
  return res >= 0x8000000000000000n ? res - 0x10000000000000000n : res;
}

const _add64s = (a,b) => _truncBigInt64(a + b)
const _sub64s = (a,b) => _truncBigInt64(a - b)
const _mul64s = (a,b) => _truncBigInt64(a * b)
const _div64s = (a,b) => _truncBigInt64(a / b)
const _shl64s = (a,b) => _truncBigInt64(a << b)
const _shr64s = (a,b) => _truncBigInt64(a >> b)

//Bits8
const _truncUInt8 = x => x & 0xff

const _truncUBigInt8 = x => Number(x & 0xffn)

const _add8u = (a,b) => (a + b) & 0xff
const _sub8u = (a,b) => (a - b) & 0xff
const _mul8u = (a,b) => (a * b) & 0xff
const _div8u = (a,b) => Math.trunc(a / b)
const _shl8u = (a,b) => (a << b) & 0xff
const _shr8u = (a,b) => (a >> b) & 0xff

//Bits16
const _truncUInt16 = x => x & 0xffff

const _truncUBigInt16 = x => Number(x & 0xffffn)

const _add16u = (a,b) => (a + b) & 0xffff
const _sub16u = (a,b) => (a - b) & 0xffff
const _mul16u = (a,b) => (a * b) & 0xffff
const _div16u = (a,b) => Math.trunc(a / b)
const _shl16u = (a,b) => (a << b) & 0xffff
const _shr16u = (a,b) => (a >> b) & 0xffff

//Bits32
const _truncUBigInt32 = x => Number(x & 0xffffffffn)

const _truncUInt32 = x => {
  const res = x & -1;
  return res < 0 ? res + 0x100000000 : res;
}

const _add32u = (a,b) => _truncUInt32(a + b)
const _sub32u = (a,b) => _truncUInt32(a - b)
const _mul32u = (a,b) => _truncUInt32(_mul32s(a,b))
const _div32u = (a,b) => Math.trunc(a / b)

const _shl32u = (a,b) => _truncUInt32(a << b)
const _shr32u = (a,b) => _truncUInt32(a <= 0x7fffffff ? a >> b : (b == 0 ? a : (a >> b) ^ ((-0x80000000) >> (b-1))))
const _and32u = (a,b) => _truncUInt32(a & b)
const _or32u = (a,b)  => _truncUInt32(a | b)
const _xor32u = (a,b) => _truncUInt32(a ^ b)

//Bits64
const _truncUBigInt64 = x => x & 0xffffffffffffffffn

const _add64u = (a,b) => (a + b) & 0xffffffffffffffffn
const _mul64u = (a,b) => (a * b) & 0xffffffffffffffffn
const _div64u = (a,b) => a / b
const _shl64u = (a,b) => (a << b) & 0xffffffffffffffffn
const _shr64u = (a,b) => (a >> b) & 0xffffffffffffffffn
const _sub64u = (a,b) => (a - b) & 0xffffffffffffffffn

//String
const _strReverse = x => x.split('').reverse().join('')

const _substr = (o,l,x) => x.slice(o, o + l)

const Prelude_Types_fastUnpack = ((str)=>__prim_js2idris_array(Array.from(str)));
const Prelude_IO_prim__putStr = (x=>process.stdout.write(x));
function x24tcOpt_1($0) {
 switch($0.a1) {
  case 0n: {
   switch($0.a2.h) {
    case undefined: return {h: 0, a1: {a1: $0.a2.a1}};
    default: return {h: 0, a1: {h: 0}};
   }
  }
  default: {
   const $8 = ($0.a1-1n);
   switch($0.a2.h) {
    case undefined: return {h: 1, a1: $8, a2: $0.a2.a2};
    default: return {h: 0, a1: {h: 0}};
   }
  }
 }
}

function Prelude_Types_getAt($0, $1) {
 return __tailRec(x24tcOpt_1, {h: 1, a1: $0, a2: $1});
}

const __mainExpression_0 = __lazy(function () {
 return PrimIO_unsafePerformIO(Main2node_main());
});

const csegen_7 = __lazy(function () {
 const $a = b => a => $b => $c => $d => {
  const $e = $b($d);
  const $11 = $c($d);
  return $e($11);
 };
 return {a1: b => a => func => $1 => $2 => Prelude_IO_map_Functor_IO(func, $1, $2), a2: a => $8 => $9 => $8, a3: $a};
});

const csegen_10 = __lazy(function () {
 return b => a => $0 => $1 => $2 => {
  const $3 = $0($2);
  return $1($3)($2);
 };
});

const csegen_13 = __lazy(function () {
 const $4 = a => $5 => $6 => {
  const $7 = $5($6);
  return $7($6);
 };
 return {a1: csegen_7(), a2: csegen_10(), a3: $4};
});

const csegen_17 = __lazy(function () {
 const $5 = a => $6 => $7 => {
  const $8 = $6($7);
  return $8($7);
 };
 const $0 = {a1: csegen_7(), a2: csegen_10(), a3: $5};
 return {a1: $0, a2: a => $e => $e};
});

const csegen_20 = __lazy(function () {
 return {a1: csegen_17(), a2: {a1: x => Prelude_Show_show_Show_String(x), a2: d => x => Prelude_Show_show_Show_String(x)}};
});

function prim__add_Integer($0, $1) {
 return ($0+$1);
}

function prim__sub_Integer($0, $1) {
 return ($0-$1);
}

function prim__mul_Integer($0, $1) {
 return ($0*$1);
}

const Main2node_y = __lazy(function () {
 return Main2node_notId({h: 'Prelude.Types.Nat'}, (Main2node_x()+1n));
});

const Main2node_x = __lazy(function () {
 return Prelude_Types_prim__integerToNat(1099956644355n);
});

function Main2node_show_ocas2($0) {
 switch($0.h) {
  case 0: return (Prelude_Show_show_Show_Int($0.a1)+'kuk');
  case 1: return ('double: '+Prelude_Show_show_Show_Double($0.a1));
  case 2: return 'nic';
 }
}

function Main2node_show_ocas($0) {
 switch($0.h) {
  case 0: return 'Bud';
  case 1: return ('Nebo'+(Prelude_Show_show_Show_Int($0.a1)+$0.a2));
  case 2: return '4sa';
  case 3: return 'das';
  case 4: return $0.a1;
 }
}

function Main2node_show_list($0) {
 switch($0.h) {
  case 0: return 0;
  case undefined: {
   switch($0.a2.h) {
    case 0: return 5;
    default: return _add32s($0.a1, Main2node_show_list($0.a2));
   }
  }
 }
}

function Main2node_notId($0, $1) {
 switch($0.h) {
  case 'Int': return _add32s($1, 1);
  case 'Main2node.Ocas2': return {h: 2};
  default: return $1;
 }
}

const Main2node_main = __lazy(function () {
 return Prelude_Interfaces_x3ex3e(csegen_13(), Prelude_IO_printLn(csegen_20(), Prelude_Show_show_Show_Integer(Main2node_y())), () => Prelude_Interfaces_x3ex3e(csegen_13(), Prelude_IO_printLn(csegen_20(), Main2node_show_ocas(Main2node_const_nebo('muf'))), () => Prelude_Interfaces_x3ex3e(csegen_13(), Prelude_IO_printLn(csegen_20(), Main2node_show_ocas2({h: 2})), () => Prelude_IO_printLn({a1: csegen_17(), a2: {a1: x => Prelude_Show_show_Show_Int(x), a2: d => x => Prelude_Show_showPrec_Show_Int(d, x)}}, Main2node_show_list({a1: 4, a2: {a1: 9, a2: {a1: 2, a2: {a1: 9, a2: {h: 0}}}}})))));
});

function Main2node_const_nebo($0) {
 return {h: 1, a1: 12, a2: $0};
}

function Builtin_snd($0) {
 return $0.a2;
}

function Builtin_fst($0) {
 return $0.a1;
}

function Builtin_believe_me($0) {
 return $0;
}

function Prelude_Types_prim__integerToNat($0) {
 let $1;
 switch(((0n<=$0)?1:0)) {
  case 0: {
   $1 = 0;
   break;
  }
  default: $1 = 1;
 }
 switch($1) {
  case 1: return Builtin_believe_me($0);
  case 0: return 0n;
 }
}

function Prelude_Types_isDigit($0) {
 switch(Prelude_EqOrd_x3ex3d_Ord_Char($0, '0')) {
  case 1: return Prelude_EqOrd_x3cx3d_Ord_Char($0, '9');
  case 0: return 0;
 }
}

function Prelude_EqOrd_compare_Ord_Integer($0, $1) {
 switch(Prelude_EqOrd_x3c_Ord_Integer($0, $1)) {
  case 1: return 0;
  case 0: {
   switch(Prelude_EqOrd_x3dx3d_Eq_Integer($0, $1)) {
    case 1: return 1;
    case 0: return 2;
   }
  }
 }
}

function Prelude_EqOrd_x3e_Ord_Char($0, $1) {
 switch((($0>$1)?1:0)) {
  case 0: return 0;
  default: return 1;
 }
}

function Prelude_EqOrd_x3ex3d_Ord_Char($0, $1) {
 switch((($0>=$1)?1:0)) {
  case 0: return 0;
  default: return 1;
 }
}

function Prelude_EqOrd_x3dx3d_Eq_Ordering($0, $1) {
 switch($0) {
  case 0: {
   switch($1) {
    case 0: return 1;
    default: return 0;
   }
  }
  case 1: {
   switch($1) {
    case 1: return 1;
    default: return 0;
   }
  }
  case 2: {
   switch($1) {
    case 2: return 1;
    default: return 0;
   }
  }
  default: return 0;
 }
}

function Prelude_EqOrd_x3dx3d_Eq_Integer($0, $1) {
 switch((($0===$1)?1:0)) {
  case 0: return 0;
  default: return 1;
 }
}

function Prelude_EqOrd_x3dx3d_Eq_Char($0, $1) {
 switch((($0===$1)?1:0)) {
  case 0: return 0;
  default: return 1;
 }
}

function Prelude_EqOrd_x3c_Ord_Integer($0, $1) {
 switch((($0<$1)?1:0)) {
  case 0: return 0;
  default: return 1;
 }
}

function Prelude_EqOrd_x3cx3d_Ord_Char($0, $1) {
 switch((($0<=$1)?1:0)) {
  case 0: return 0;
  default: return 1;
 }
}

function Prelude_EqOrd_x2fx3d_Eq_Ordering($0, $1) {
 switch(Prelude_EqOrd_x3dx3d_Eq_Ordering($0, $1)) {
  case 1: return 0;
  case 0: return 1;
 }
}

function Prelude_Interfaces_x3ex3e($0, $1, $2) {
 return $0.a2(undefined)(undefined)($1)($c => $2());
}

function Prelude_Show_n__2319_9601_asciiTab($0) {
 return {a1: 'NUL', a2: {a1: 'SOH', a2: {a1: 'STX', a2: {a1: 'ETX', a2: {a1: 'EOT', a2: {a1: 'ENQ', a2: {a1: 'ACK', a2: {a1: 'BEL', a2: {a1: 'BS', a2: {a1: 'HT', a2: {a1: 'LF', a2: {a1: 'VT', a2: {a1: 'FF', a2: {a1: 'CR', a2: {a1: 'SO', a2: {a1: 'SI', a2: {a1: 'DLE', a2: {a1: 'DC1', a2: {a1: 'DC2', a2: {a1: 'DC3', a2: {a1: 'DC4', a2: {a1: 'NAK', a2: {a1: 'SYN', a2: {a1: 'ETB', a2: {a1: 'CAN', a2: {a1: 'EM', a2: {a1: 'SUB', a2: {a1: 'ESC', a2: {a1: 'FS', a2: {a1: 'GS', a2: {a1: 'RS', a2: {a1: 'US', a2: {h: 0}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}};
}

function Prelude_Show_show_Show_String($0) {
 return ('\"'+Prelude_Show_showLitString(Prelude_Types_fastUnpack($0), '\"'));
}

function Prelude_Show_show_Show_Integer($0) {
 return Prelude_Show_showPrec_Show_Integer({h: 0}, $0);
}

function Prelude_Show_show_Show_Int($0) {
 return Prelude_Show_showPrec_Show_Int({h: 0}, $0);
}

function Prelude_Show_show_Show_Double($0) {
 return Prelude_Show_showPrec_Show_Double({h: 0}, $0);
}

function Prelude_Show_showPrec_Show_Integer($0, $1) {
 return Prelude_Show_primNumShow($4 => (''+$4), $0, $1);
}

function Prelude_Show_showPrec_Show_Int($0, $1) {
 return Prelude_Show_primNumShow($4 => (''+$4), $0, $1);
}

function Prelude_Show_showPrec_Show_Double($0, $1) {
 return Prelude_Show_primNumShow($4 => (''+$4), $0, $1);
}

function Prelude_Show_compare_Ord_Prec($0, $1) {
 switch($0.h) {
  case 4: {
   switch($1.h) {
    case 4: return Prelude_EqOrd_compare_Ord_Integer($0.a1, $1.a1);
    default: return Prelude_EqOrd_compare_Ord_Integer(Prelude_Show_precCon($0), Prelude_Show_precCon($1));
   }
  }
  default: return Prelude_EqOrd_compare_Ord_Integer(Prelude_Show_precCon($0), Prelude_Show_precCon($1));
 }
}

function Prelude_Show_x3ex3d_Ord_Prec($0, $1) {
 return Prelude_EqOrd_x2fx3d_Eq_Ordering(Prelude_Show_compare_Ord_Prec($0, $1), 0);
}

function Prelude_Show_showParens($0, $1) {
 switch($0) {
  case 0: return $1;
  case 1: return ('('+($1+')'));
 }
}

function Prelude_Show_showLitString($0, $1) {
 switch($0.h) {
  case 0: return $1;
  case undefined: {
   switch($0.a1) {
    case '\"': return ('\u{5c}\"'+Prelude_Show_showLitString($0.a2, $1));
    default: return Prelude_Show_showLitChar($0.a1)(Prelude_Show_showLitString($0.a2, $1));
   }
  }
 }
}

function Prelude_Show_showLitChar($0) {
 switch($0) {
  case '\u{7}': return $2 => ('\u{5c}a'+$2);
  case '\u{8}': return $5 => ('\u{5c}b'+$5);
  case '\u{c}': return $8 => ('\u{5c}f'+$8);
  case '\n': return $b => ('\u{5c}n'+$b);
  case '\r': return $e => ('\u{5c}r'+$e);
  case '\u{9}': return $11 => ('\u{5c}t'+$11);
  case '\u{b}': return $14 => ('\u{5c}v'+$14);
  case '\u{e}': return $17 => Prelude_Show_protectEsc($1a => Prelude_EqOrd_x3dx3d_Eq_Char($1a, 'H'), '\u{5c}SO', $17);
  case '\u{7f}': return $20 => ('\u{5c}DEL'+$20);
  case '\u{5c}': return $23 => ('\u{5c}\u{5c}'+$23);
  default: {
   return $26 => {
    const $27 = Prelude_Types_getAt(Prelude_Types_prim__integerToNat(BigInt($0.codePointAt(0))), Prelude_Show_n__2319_9601_asciiTab($0));
    switch($27.h) {
     case undefined: return ('\u{5c}'+($27.a1+$26));
     case 0: {
      switch(Prelude_EqOrd_x3e_Ord_Char($0, '\u{7f}')) {
       case 1: return ('\u{5c}'+Prelude_Show_protectEsc($3c => Prelude_Types_isDigit($3c), Prelude_Show_show_Show_Int(_truncInt32($0.codePointAt(0))), $26));
       case 0: return ($0+$26);
      }
     }
    }
   };
  }
 }
}

function Prelude_Show_protectEsc($0, $1, $2) {
 let $5;
 switch(Prelude_Show_firstCharIs($0, $2)) {
  case 1: {
   $5 = '\u{5c}&';
   break;
  }
  case 0: {
   $5 = '';
   break;
  }
 }
 const $4 = ($5+$2);
 return ($1+$4);
}

function Prelude_Show_primNumShow($0, $1, $2) {
 const $3 = $0($2);
 let $7;
 switch(Prelude_Show_x3ex3d_Ord_Prec($1, {h: 5})) {
  case 1: {
   $7 = Prelude_Show_firstCharIs($e => Prelude_EqOrd_x3dx3d_Eq_Char($e, '-'), $3);
   break;
  }
  case 0: {
   $7 = 0;
   break;
  }
 }
 return Prelude_Show_showParens($7, $3);
}

function Prelude_Show_precCon($0) {
 switch($0.h) {
  case 0: return 0n;
  case 1: return 1n;
  case 2: return 2n;
  case 3: return 3n;
  case 4: return 4n;
  case 5: return 5n;
  case 6: return 6n;
 }
}

function Prelude_Show_firstCharIs($0, $1) {
 switch($1) {
  case '': return 0;
  default: return $0(($1.charAt(0)));
 }
}

function Prelude_IO_map_Functor_IO($0, $1, $2) {
 const $3 = $1($2);
 return $0($3);
}

function Prelude_IO_putStrLn($0, $1) {
 return Prelude_IO_putStr($0, ($1+'\n'));
}

function Prelude_IO_putStr($0, $1) {
 return $0.a2(undefined)($7 => Prelude_IO_prim__putStr($1, $7));
}

function Prelude_IO_printLn($0, $1) {
 const $7 = Builtin_snd($0);
 const $6 = $7.a1($1);
 return Prelude_IO_putStrLn(Builtin_fst($0), $6);
}

function PrimIO_unsafePerformIO($0) {
 return PrimIO_unsafeCreateWorld(w => $0(w));
}

function PrimIO_unsafeCreateWorld($0) {
 return $0(_idrisworld);
}


try{__mainExpression_0()}catch(e){if(e instanceof IdrisError){console.log('ERROR: ' + e.message)}else{throw e} }
