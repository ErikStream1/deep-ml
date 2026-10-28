import numpy as np

def l1(arr: np.ndarray)->float:
    if arr.shape == (2,2):
        arr = arr.ravel()
        return np.linalg.norm(arr, ord=1)

    return np.linalg.norm(arr, ord=1)
def l2(arr: np.ndarray)->float:
    if arr.shape == (2,2):
        arr = arr.ravel()
        return np.linalg.norm(arr, ord=2)

    return np.linalg.norm(arr, ord=2)

def linf(arr: np.ndarray)->float:
    if arr.shape == (2,2):
        arr = arr.ravel()
        return np.linalg.norm(arr, ord=np.inf)

    return np.linalg.norm(arr, ord=np.inf)

def frobenius(arr: np.ndarray)->float:
    if arr.shape != (2,2):
       raise ValueError("Error")

    return np.linalg.norm(arr, ord="fro")

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
   match norm_type:
    case "l1":
        return l1(arr)
    case "l2":
        return l2(arr)
    case "linf":
        return linf(arr)
    case "frobenius":
        return frobenius(arr)
    case _:
        raise ValueError("Error")
    