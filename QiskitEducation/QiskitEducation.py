# coding: utf-8

# Copyright © 2018 IBM Research

# Adapted from and/or inspired by
# * initialization tool by Mirko Amico
#   https://github.com/Qiskit/qiskit-tutorials/blob/awards/community/awards/teach_me_quantum_2018/intro2qc/initialize.py
# * qreative by James R. Wootton
#   https://github.com/quantumjim/qreative/blob/master/qreative/qreative.py


from qiskit import *
from qiskit.tools.visualization import plot_histogram as plothistogram

def get_backend(device):
    """Returns backend object for device specified by input string."""
    try:
        try:
            backend = Aer.get_backend(device)
        except:
            backend = BasicAer.get_backend(device)
    except:
        backend = IBMQ.get_backend(device)
    return backend


def get_noise(noisy):
    """Returns a noise model when input is not False or None.
    A string will be interpreted as the name of a backend, and the noise model of this will be extracted.
    A float will be interpreted as an error probability for a depolarizing+measurement error model.
    Anything else (such as True) will give the depolarizing+measurement error model with default error probabilities."""
    if noisy:

        if type(noisy) is str:
            device = get_backend(noisy)
            noise_model = noise.device.basic_device_noise_model( device.properties() )
        else:
            if type(noisy) is float:
                p_meas = noisy
                p_gate1 = noisy
            else:
                p_meas = 0.08
                p_gate1 = 0.04

            error_meas = pauli_error([('X',p_meas), ('I', 1 - p_meas)])
            error_gate1 = depolarizing_error(p_gate1, 1)
            error_gate2 = error_gate1.kron(error_gate1)

            noise_model = NoiseModel()
            noise_model.add_all_qubit_quantum_error(error_meas, "measure")
            noise_model.add_all_qubit_quantum_error(error_gate1, ["u1", "u2", "u3"])
            noise_model.add_all_qubit_quantum_error(error_gate2, ["cx"])

    else:
        noise_model = None
    return noise_model


class QuantumAlgorithm:
    """"""
    def __init__ (self, qregs, cregs):

        qubit = {}
        if type(qregs)!=list:
            qregs = [(qregs,'q')]

        if type(cregs)!=list:
            cregs = [(cregs,'c')]

        self.qc = QuantumCircuit()

        for qreg in qregs:
            exec( 'self.'+qreg[1]+'=QuantumRegister('+str(qreg[0])+',"'+str(qreg[1])+'")' )
            exec( 'self.qc.add_register( self.'+qreg[1]+')' )

        for creg in cregs:
            exec( 'self.'+creg[1]+'=ClassicalRegister('+str(creg[0])+',"'+str(creg[1])+'")' )
            exec( 'self.qc.add_register( self.'+creg[1]+')' )

    # methods to implement the methods of qc, in exactly the same manner as terra 0.7
    def x(self,qubit):
        self.qc.x(qubit)
    def y(self,qubit):
        self.qc.y(qubit)
    def z(self,qubit):
        self.qc.z(qubit)
    def h(self,qubit):
        self.qc.h(qubit)
    def s(self,qubit):
        self.qc.s(qubit)
    def sdg(self,qubit):
        self.qc.sdg(qubit)
    def t(self,qubit):
        self.qc.t(qubit)
    def tdg(self,qubit):
        self.qc.tdg(qubit)
    def cx(self,control,target):
        self.qc.cx(control,target)
    def cz(self,control,target):
        self.qc.cz(control,target)
    def ccx(self,control1,control2,target):
        self.qc.cx(control1,control2,target)
    def measure(self,qubit,bit):
        self.qc.measure(qubit,bit)

    def execute(self,device='qasm_simulator',noisy=False,shots=1024,histogram=True):

        backend = get_backend(device)
        try:
            job = execute(self.qc,backend,shots=shots,noise_model=get_noise(noisy),memory=True)
            data = {'counts':job.result().get_counts(),'memory':job.result().get_memory()}
        except:
            try:
                job = execute(self.qc,backend,shots=shots,memory=True)
                data = {'counts':job.result().get_counts(),'memory':job.result().get_memory()}
            except:
                job = execute(self.qc,backend,shots=shots)
                data = {'counts':job.result().get_counts()}

        if histogram:
            self.plot_histogram(data['counts'])

        return data

    def plot_histogram(self,counts):
        return plothistogram(counts)
