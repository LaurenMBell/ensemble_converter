import pytest
import pandas as pd
from ensembl_converter.converter import EnsemblConverter

def test1_fetch():
    converter = EnsemblConverter()
    assert converter.fetch("ENSG00000139618") == "BRCA2"

def test2_fetch():
    converter = EnsemblConverter()
    assert converter.fetch("ENSG00000157764") == "BRAF"
    
def test1_fetch_many():
    converter = EnsemblConverter()
    ensembl_ids = ["ENSG00000139618", "ENSG00000157764", "ENSG00000198712",
                   "ENSG00000248378", "ENSG00000141510", "ENSG00000162444",
                   "ENSG00000171862", "ENSG00000134982", "ENSG00000125844",
                   "ENSG00000170471"]
    expected_symbols = ["BRCA2", "BRAF", "TP53", "EGFR", "MYC", "KRAS", "PTEN", 
                      "CDK2", "STAT3", "GATA3"]
    
    expected_df = pd.DataFrame({
        "Ensembl ID": ensembl_ids,
        "Gene Symbol": expected_symbols
    })
    
    result_df = converter.fetch_many(ensembl_ids)
    
    pd.testing.assert_frame_equal(result_df, expected_df)

def test2_fetch_many():
    converter = EnsemblConverter()
    ensembl_ids = ["ENSG00000277454", "ENSG00000111249", "ENSG00000130764",
                   "ENSG00000165699", "ENSG00000204231", "ENSG00000105246",
                   "ENSG00000134352", "ENSG00000165029", "ENSG00000172053",
                   "ENSG00000121892"]
    expected_symbols = ["MDM2", "FOXP3", "CDKN1A", "PIK3CA", "SOX2",
                      "SMAD4", "NF1", "APC", "NOTCH1", "JAK2"]
    
    expected_df = pd.DataFrame({
        "Ensembl ID": ensembl_ids,
        "Gene Symbol": expected_symbols
    })

    result_df = converter.fetch_many(ensembl_ids)
    
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_fetch_with_info():
    converter = EnsemblConverter()
    ensembl_ids = ["ENSG00000277454", "ENSG00000111249", "ENSG00000130764"]

    addit_data = ['chromosome_name', 'gene_biotype']

    result_df = converter.fetch_with_info(ensembl_ids, addit_data)

    expected_data = {
        "Ensembl ID": ["ENSG00000277454", "ENSG00000111249", "ENSG00000130764"],
        "Gene Symbol": ["MDM2", "FOXP3", "CDKN1A"],
        "chromosome_name": ["12", "X", "6"], 
        "gene_biotype": ["protein_coding", "protein_coding", "protein_coding"]
    }
    expected_df = pd.DataFrame(expected_data)

    pd.testing.assert_frame_equal(result_df, expected_df)


