from functools import reduce
import itertools
import random
import numpy as np


class QuaSimpleCircuit:
    """
    All-in-one circuit class which initialises the qubits and loads
    all basic gates ready to be applied on desired qubit.\n

    params: numQubits (Number of Qubits required)
    """

    def __init__(self, numQubits):
        """
        Initialising some variables which are scoped through out the quantum register
        """
        self.numQubits = numQubits
        self.probabilities = []
        self.i = np.complex_(2)
        self.I = np.identity(2)

        #Creating |0>
        self.q0 = np.array([1, 0])

        #Fancy way to create initial state vector
        self.stateVector = reduce(
            np.kron, [self.q0 for _ in range(self.numQubits)])

        #Creating a list of all the possible outcomes
        self.indexBin = [reduce(lambda x, y: str(x)+str(y), i)
                         for i in itertools.product([0, 1], repeat=self.numQubits)]

    def X(self, qubit):
        """
        Pauli-X gate flips the value of the qubit. It is quantum equivalent to
        classical NOT gate.\n

        params: qubit (Target qubit)
        """
        x = np.matrix([
            [0, 1],
            [1, 0]
        ])
        O = reduce(
            np.kron, [x if i == qubit else self.I for i in range(self.numQubits)])

        self.stateVector = np.dot(self.stateVector, O)

    def H(self, qubit):
        """
        Haddamard gate puts the qubit in a superposition state.\n
        
        params: qubit (Target qubit)
        """
        h = np.multiply(1. / np.sqrt(2), np.matrix([
            [1, 1],
            [1, -1]
        ]))

        O = reduce(
            np.kron, [h if i == qubit else self.I for i in range(self.numQubits)])

        self.stateVector = np.dot(self.stateVector, O)

    def Y(qubit):
        """
        Pauli-Y gate rotates the qubit along Y-axis by PI radians.\n
        
        params: qubit (Target qubit)
        """
        y = np.matrix([
            [1, 0],
            [0, -1]
        ])

        O = reduce(
            np.kron, [y if i == qubit else self.I for i in range(self.numQubits)])

        self.stateVector = np.dot(self.stateVector, O)

    def Z(qubit):
        """
        Pauli-Z gate rotates the qubit along Z-axis by PI radians.\n
        
        params: qubit (Target qubit)\n
        """
        z = np.matrix([
            [1, 0],
            [0, -1]
        ])

        O = reduce(
            np.kron, [z if i == qubit else self.I for i in range(self.numQubits)])

        self.stateVector = np.dot(self.stateVector, O)

    def S(qubit):
        """
        S-gate is a R-phi gate with phi=PI/2.
        It essentials rotates the qubit by a quarter.\n
        
        params: qubit (Target qubit)\n
        """
        s = np.matrix([
            [1, 0],
            [o, i]
        ])

        O = reduce(
            np.kron, [s if i == qubit else self.I for i in range(self.numQubits)])

        self.stateVector = np.dot(self.stateVector, O)

    def T(qubit):
        """
        T-gate is a R-phi gate with phi=PI/4.\n
        
        params: qubit (Target qubit)\n
        """
        t = np.matrix([
            [1, 0],
            [0, np.e**(i * np.pi / 4.)]
        ])

        O = reduce(
            np.kron, [s if i == qubit else self.I for i in range(self.numQubits)])

        self.stateVector = np.dot(self.stateVector, O)

    def CX(self, controlQubit, targetQubit=1):
        """
        CNOT gate is a conditional gate that performs X-gate on the target qubit
        if the control gate is |1> .\n
        
        params: qubit (Target qubit)\n
        """
        I = np.identity(2)

        P0x0 = np.array([
            [1, 0],
            [0, 0]
        ])

        P1x1 = np.array([
            [0, 0],
            [0, 1]
        ])

        X = np.matrix([
            [0, 1],
            [1, 0]
        ])

        #For implementing CNOT gate in a m-qubit circuit
        O1 = reduce(
            np.kron, [P0x0 if i == controlQubit else self.I for i in range(self.numQubits)])

        O2 = reduce(
            np.kron, [P1x1 if i == controlQubit else(X if i == targetQubit else I) for i in range(self.numQubits)])

        O = O1 + O2

        self.stateVector = np.dot(self.stateVector, O)

    def measure(self):
        """
        Returns the current state vector
        """
        print(self.stateVector)

    def get_counts(self, num_shots=100):
        """
        Executes multi-shot measurement of qubits using weighted random technique.\n

        params: num_shots (Number of shots). Default is 100.
        """
        count = {}
        outcome = {}
        for idx, index in enumerate(self.indexBin):
            if self.stateVector[0, idx] != 0.:
                count[index] = self.stateVector[0, idx]
                outcome[index] = 0
                self.probabilities.append(self.stateVector[0, idx] ** 2)

        for _ in range(num_shots):
            outcome[random.choices(
                [i for i in count.keys()], self.probabilities)[0]] += 1

        print(outcome)
