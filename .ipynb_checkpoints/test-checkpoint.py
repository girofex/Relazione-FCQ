from qiskit import QuantumCircuit

#Create quantum circuit qith 3 qubits and 3 classical bits:
qc = QuantumCircuit(3, 3)
qc.x([0,1]) #Perform X-gates on qubits 0 & 1
qc.draw()   #returns a drawing of the circuit



#second version
qc.measure([0,1,2], [0,1,2])
qc.draw()





#import Qiskit's simulator Aer and make a new simulator object
from qiskit import Aer

#run the quantum circuit on a state vector simulator backend
backend = Aer.get_backend('statevector_simulator')  #make new simulator object
job = backend.run(qc)   #run the experiment
result = job.result()   #get the result
outputstate = result.get_counts()   #interpret the results as a "counts" dictionary





#Quantum adder
test_qc = QuantumCircuit(4, 2)

#First, our circuit should encode an input (here '11')
test_qc.x(0)
test_qc.x(1)

#Next, it should carry out the adder circuit we created
test_qc.cx(0, 2)
test_qc.cx(1, 2)
test_qc.ccx(0, 1, 3)

#Finally, we will measure the bottom two qubits to extract the output
test_qc.measure(2, 0)
test_qc.measure(3, 1)
test_qc.draw()