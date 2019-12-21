// JUMSCRIPT FOR DAY 21 PART 2
// A or B or C:
// There is a gap somewhere in the next 3 tiles so we need to jump
or A T
and B T
and C T
not T J
// . and D
// We don't die if we jump
and D J
// (postfix)
// . and (H or EI or EF)
//   H : We can immediatly jump again
//   EI: We can walk one step and then jump again
//   EF: We can walk two steps (and then potentially jump again)
// We don't have any information about tiles after I so we ignore and hope for
// the best
not F T
not T T
or I T
and E T
or H T
and T J
run
