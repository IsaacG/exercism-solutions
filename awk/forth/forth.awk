#!/usr/bin/env gawk -f
#

@include "join"

# -- Helper functions -- #

function pop() { return stack[depth--]; }
function push(val) { stack[++depth] = val; }
function die(msg) { print msg; exit 1; }

# -- Print stack and reset state -- #
function dump_stack_and_reset() {
    if (depth) print join(stack, 1, depth, " ")
    delete stack
    delete macro
    depth = 0
}

# Print stack and reset the state between files and at the end.
FNR == 1 && NR > 1 { dump_stack_and_reset() }
END { dump_stack_and_reset() }

# Ignore case.
{ $0 = toupper($0) }

# Macro definitions.
$1 == ":" {
    if ($NF != ";") die("macro not terminated with semicolon")
    if ($2 + 0 == $2) die("illegal operation")
    if (NF < 4) die("empty macro definition")

    expansion = ""
    for (i = 3; i < NF; i++)
        if ($i in macro)
            expansion = expansion macro[$i] " "
        else
            expansion = expansion $i " "
    macro[$2] = expansion
    # Stop processing.
    next
}

# Non-macro "regular" statements.
{
    # Expand macros
    for (i = 1; i <= NF; i++)
        if ($i in macro)
            $i = macro[$i]
    # Re-split the fields.
    $0 = $0
    for (i = 1; i <= NF; i++) {
        # Check for sufficient stack depth.
        switch ($i) {
            case /^([-+*/]|SWAP|OVER)$/: 
                if (depth == 1)
                    die("only one value on the stack")
            case /^(DUP|DROP)$/: 
                if (depth == 0)
                    die("empty stack")
        }

        if ($i + 0 == $i) {
            # Numbers.
            push($i)
        } else if ($i ~ /^[+*/-]$/) {
            # Arithmetic operators.
            b = pop(); a = pop()
            switch($i) {
                case "+": push(a + b); break
                case "-": push(a - b); break
                case "*": push(a * b); break
                case "/":
                    if (b == 0) die("divide by zero")
                    push(int(a / b))
                    break
            }
        } else if ($i ~ /^(DUP|DROP|SWAP|OVER)$/) {
            # Stack operators.
            if ($i ~ /^(SWAP|OVER)$/) b = pop()
            a = pop()
            switch($i) {
                case "DROP": break
                case "DUP":  push(a); push(a); break
                case "SWAP": push(b); push(a); break
                case "OVER": push(a); push(b); push(a); break
            }
        } else {
            die("undefined operation")
        }
    }
}
