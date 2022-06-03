# Coordinates Analyzer

### :warning: Disclaimer

---

Coordinate_Analyzer is a **(working in progress)** CLI Python program. Soon it will be finished and uploaded do PyPI.

### :dart: Basic Information  

---

The main objective of the program it is to compare 2 molecular structures, based on their atomic coordinates, and do a simply (but efficient) mathematical comparasion througout RMSD (root-mean-square deviation) and Kabsch algorithm.    

Two of the major aspects here it is to be able to tell the differences between 2 molecular structures after they have gone through any geometry modification, and, avaliate their similarity and compatibility. For example, comparing the final molecular geometry, after a optimization process, with the starting one; or, for the bioinformatics, compare 2 protein structures and their equivalence.  

<!--
:dart: Considering two sets of atomic coordinates (P and Q): 

- P = coordinates system after *some* process; 
- Q = coordinates system from *reference*; 
- align both coordinates systems to the *same* centroid; (**translation process**)
- calculate the optimal coordinates system between both matrices; (**transposing the reference (*Q*)**)
- calculate the SVD of the optimal coordinates system; 
- generate 3 matrices from SVD: 
    - U = 
    - S = 
    - Vt = 
-->



