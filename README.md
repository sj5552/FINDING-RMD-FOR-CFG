## Finding the Right Most Derivative for a given CFG (Context Free Grammar) Using Python programming.

### Objective of Problem
The objective is to provide a structured and systematic way to illustrate how a given string is derived from a CFG, emphasizing right-most symbol replacement and adherence to the grammar's rules.

### Flow Chart
!Alt text

### Explanation
def rightmostDerivation(cfg, string):
    """
    Given a Context Free Grammar (CFG) and a string, this function returns the rightmost derivation of the string from the CFG.
    """
    # Start with the initial symbol
    derivation = cfg.start()
    
    # Keep replacing rightmost non-terminals with their production rules until only terminals remain
    while any([symbol in derivation for symbol in cfg.nonterminals()]):
        for symbol in reversed(derivation):
            if symbol in cfg.nonterminals():
                production = cfg.productions(rhs=symbol)[0]
                derivation = derivation.replace(symbol, production.rhs(), 1)
                break
    
    return derivation

