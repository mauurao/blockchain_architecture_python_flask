# Supply Chain: Blockchain

   <h3><b>Blockchain Prototype for a Semi-Private Supply Chain</b></h3>
    <h4>Rastreability and Traceability of Medicines</h4>
    <h5><small>Created by Mauro Cardoso using Python and Flask, ©2022</small></h5>
    <h6><small><br><br>
        Flask application created for a healthcare supply chain, using the concepts of blockchain technology
        <br><br>
        <strong>This chain simulates the transactions between actors (Hard-coded) with their respective amounts.<br> It does not manage them or the interveners' wallets.</strong><br>
        <strong>These transactions create a hash for each of the data involved in the transaction.</strong><br>
        <strong>Each hash generates a JSON file with the details of the transaction for a folder, thus acting as the ledger.</strong><br><br>
        This network is supposed to be semi-private so the spaces below, simulate the spaces reserved for each participant,<br> 
        being this number reduced there is a faster consensus and a higher transaction transfer rate and greater scalability.<br> 
        If there is a change in interactions it can be easy discovered through the chain, or business needs, participant access can be modified with ease.<br>
        There is an obstacle in this implementation as it does not have a logic of permissions applied to the actors in the network.<br><br>
        The management of a B2B or enterprise network like this is managed by a regulator (Admin).
        <br><br>
