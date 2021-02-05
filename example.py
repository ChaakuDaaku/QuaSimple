from QuaSimple import QuaSimpleCircuit

Deutsch = QuaSimpleCircuit(3)
Deutsch.H(0)
Deutsch.H(1)
Deutsch.X(2)
Deutsch.H(2)
Deutsch.CX(0, 2)
Deutsch.CX(1, 2)
Deutsch.H(2)
Deutsch.H(0)
Deutsch.H(1)
Deutsch.X(2)
Deutsch.get_counts(100)
