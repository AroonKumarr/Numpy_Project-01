import numpy as np

 
matrix = np.array(eval(input("Enter matrix as a list of lists: ")))

print("\nSelect an operation:")
print("1. Determinant")
print("2. Inverse")
print("3. Eigenvalues & Eigenvectors")
print("4. Solve a System (Ax = B)")

ask = int(input("\nChoose an option (1-4): "))

try:
    if ask == 1:
        if matrix.shape[0] == matrix.shape[1]:  
            print("\nDeterminant:", np.linalg.det(matrix))
        else:
            print("\nDeterminant can only be calculated for square matrices.")
    
    elif ask == 2:
        if matrix.shape[0] == matrix.shape[1]:
            print("\nInverse:\n", np.linalg.inv(matrix))
        else:
            print("\nInverse can only be calculated for square matrices.")
    
    elif ask == 3:
        if matrix.shape[0] == matrix.shape[1]:
            eigenvalues, eigenvectors = np.linalg.eig(matrix)
            print("\nEigenvalues:", eigenvalues)
            print("\nEigenvectors:\n", eigenvectors)
        else:
            print("\nEigenvalues & Eigenvectors require a square matrix.")
    
    elif ask == 4:
         
        B = np.array(eval(input("Enter B as a list: ")))
        
        if matrix.shape[0] == matrix.shape[1]:  
            if matrix.shape[0] == B.shape[0]:   
                solution = np.linalg.solve(matrix, B)
                print("\nSolution for Ax = B:\n", solution)
            else:
                print("\nB must have the same number of rows as A.")
        else:
            print("\nMatrix A must be square to solve Ax = B.")

    else:
        print("\nInvalid option. Please choose 1-4.")

except np.linalg.LinAlgError as e:
    print("\nError:", e)

