import pandas as pd
from biomart import BiomartServer 

class EnsemblCoverter:
    def __init__(self):
        self.server = BiomartServer("http://www.ensembl.org/biomart")
        self.ensembl = self.server.datasets['hsapiens_gene_ensembl']
    
    def fetch(self, ensembl_ids):
        results = self.ensembl.query(
            attributes=['ensembl_gene_id', 'hgnc_symbol'],
            filters={'ensembl_gene_id': ensembl_ids}
        )
        
        for line in results.splitlines():
            fields = line.split('\t')
            if len(fields) == 2 and fields[1]:
                return fields[1]
        return None
    
    def fetch_many(self, ensembl_ids):
        results = self.dataset.query(
        attributes=['ensembl_gene_id', 'hgnc_symbol'],
        filters={'ensembl_gene_id': ensembl_ids}
    )
    
        data = []
        for line in results.splitlines():
            fields = line.split("\t")
            if len(fields) == 2:
                ensembl_id, gene_symbol = fields
                if gene_symbol:
                    data.append((ensembl_id, gene_symbol))
    
        return pd.DataFrame(data, columns=["Ensembl ID", "Gene Symbol"])

    def fetch_with_info(self, ensembl_ids, addit_data):
        if addit_data is None:
            addit_data = []

        results = self.ensembl.query(
            attributes=['ensembl_gene_id', 'hgnc_symbol'] + addit_data,
            filters={'ensembl_gene_id': ensembl_ids}
        )
        
        data = []
        for line in results.splitlines():
            fields = line.split("\t")
            if len(fields) >= 2:
                ensembl_id, gene_symbol = fields[:2]
                additional_data = fields[2:]
                if gene_symbol:
                    data.append([ensembl_id, gene_symbol] + additional_data)
        
        columns = ["Ensembl ID", "Gene Symbol"] + addit_data
        return pd.DataFrame(data, columns=columns)
        
    def to_file(self, gene_symbols_df, output_filename):
        gene_symbols_df.to_csv(output_filename)
        print(f"Gene symbols saved to {output_filename}")

