# SimpleIOTA

### Implementation notes:

* The main objects are the Node, wallet(light node) and the Tangle
* Both nodes and wallets can initiate transactions.
* A node can have more than one wallets.
* A wallet can exist in our outside a fullNode. When inside a node its a wallet and when outside its refered to as a light-node. 


### Additional nodes:

* When a node isues a transaction, it must confirm at least 2 other transactions before its transaction can be added to the tangle.
* To confirm a transaction, the node must check for conflict. If the transaction has conflict then the node must not approve it.
* When a node issues a transaction it must solve a crypto puzzle for this transaction to be considered valid. 
	This is achieved by nding a nonce such that the hash of that nonce concatenated with 	  some data from the approved transaction has a particular form. In the case of the    Bitcoin protocol, the hash must have at least a predened number of leading zeros.  

* A transaction must have a weight property:

* A transaction must have cumulative weight. Cumulative weight  =  weight of transaction + own weights of all transactions that directly or iderectly approves it.

* Tips = Total number of unapproved transactions in the system at any time t

* Any node, at the moment when it issues a transaction, observes not the actual state of the tangle, but the one exactly h time units ago. This means, in particular, that a transaction attached to the tangle at time t only becomes visible to the network at time t+h.

* A tip can be in hidden or revealed state. A transaction attached at time t remains in hidden state until time t+h when it then moves to revealed state.

* Consider large weight attack: This is a threat when large weight is used as a basis for tips selection in the tip selection algorithm.

