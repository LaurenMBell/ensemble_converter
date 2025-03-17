from .converter import EnsemblConverter

# ensembl_converter/__init__.py
from .converter import EnsemblConverter

# Easy access to the main function
def fetch(ensembl_id):
    """
    Quick function to fetch a gene symbol for a single Ensembl ID.
    
    Args:
        ensembl_id (str): An Ensembl gene ID
        
    Returns:
        str: The corresponding gene symbol or None if not found
    """
    converter = EnsemblConverter()
    return converter.fetch(ensembl_id)

def fetch_many(ensembl_ids):
    """
    Quick function to fetch gene symbols for multiple Ensembl IDs.
    
    Args:
        ensembl_ids (list): List of Ensembl gene IDs
        
    Returns:
        pandas.DataFrame: DataFrame with Ensembl IDs and gene symbols
    """
    converter = EnsemblConverter()
    return converter.fetch_many(ensembl_ids)