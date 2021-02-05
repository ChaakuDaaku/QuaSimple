# QuaSimple

QuaSimple is a very simple quantum simulator which is capable of computing n-qubits with variety of available quantum gates to play with.

## Syntax

### Initialising the circuit register
```python
#Initialise the quantum register by creating an object of the QuaSimple class
#and passing the required number of qubits required as a parameter.
example = QuaSimpleCircuit(3)
```

### Performing operation on the qubit
```python
example.X(0)
example.Y(0)
example.Z(0)
example.H(0)
example.S(0)
example.T(0)
example.CX(0,1)
```

### Measuring the qubits
```python
#The state vector of the register can be obtained by using measure function.
example.measure()

#Multi-shot measurement can be done by calling get_counts function.
#Number of shots are needed to be passed
example.get_counts(1000)
```

## Demo Example
```python

from QuaSimple import QuaSimpleCircuit

#------------------------------#
#       Swap Qubits            #
#------------------------------#
#In this experiment we will swap the state
#of the first qubit to second qubit

#Initialise the circuit
Swap = QuaSimpleCircuit(2)

#Flip the 1st qubit to create |10>
Swap.X(0)

#Perform desired quantum operations
Swap.CX(0,1)
Swap.H(0)
Swap.H(1)
Swap.CX(0,1)
Swap.H(0)
Swap.H(1)
Swap.CX(0,1)

#Get multi-shot measurement
Swap.get_counts(100)

```
### Output
```
{'01': 100, '10': 0}
```

## DIY
Try running Deutsch-Jozsa algorithm pre-written in QuaSimple.
```bash
python example.py
```

## TODO
- Refactor Code
- Document properly
- Add more gates
