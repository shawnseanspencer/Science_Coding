#Gram-Schmidt Procedure Code
import numpy as np

def normalized(vec):
    vec = np.array(vec)
    normalized_vector = vec/np.linalg.norm(vec)
    return normalized_vector

def proj(u, v):
    u, v = np.array(u), np.array(v)
    projection = np.dot(u,v)/np.linalg.norm(v)**2 * v
    return projection

def gram_schmidt(*args):
    n = len(args)
    vectors = []
    for i in range(n):
        veci = np.array(args[i])
        perp_vector = args[i]
        if i != 0:
            for j in range(len(vectors)):
                if i != j:
                    projection = proj(args[i], vectors[j])
                    perp_vector += -projection
        vectors.append(normalized(perp_vector))


    return vectors
                    
#Example Vectors 
x = [2,0,3,1,2,4]
y = [1,10,12,5,4,0]
z = [1,2,3,4,5,6]

orthonormal_basis = gram_schmidt(x,y,z)
print(orthonormal_basis)

for i in range(len(orthonormal_basis)):
    print(f"Checking Norm of Basis Vector {i} = 1:", np.linalg.norm(orthonormal_basis[i]))
    for j in range(len(orthonormal_basis)):
        if i!= j:
            #A bit redundant but idc
            print(f"Checking Orthogonality between vector {i} and vector {j}:", np.dot(orthonormal_basis[i],orthonormal_basis[j]))

