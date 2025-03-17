import pandas as pd
from biomart import BiomartServer 

class EnsemblConverter:
    #initialize the class attributes
    def __init__(self):
        self.server = BiomartServer("http://www.biomart.org/biomart")
        self.ensembl = self.server.datasets['hsapiens_gene_ensembl']
        self.server.verbose = True
        self.cache = {}
    
    #return one ID's symbol
    def fetch(self, ensembl_id):
        #if its in the cache, use that
        if ensembl_id in self.cache:
            return self.cache[ensembl_id]
        
        #if not, get it from the API
        results = self.ensembl.search(
            attributes=['ensembl_gene_id', 'hgnc_symbol'],
            filters={'ensembl_gene_id': ensembl_id}
        )
        
        for line in results.splitlines():
            fields = line.split('\t')
            if len(fields) == 2 and fields[1]:
                return fields[1]
        return None
    
    #fetch multiple ID's sybmols at once
    def fetch_many(self, ensembl_ids):
        ids = []
        symbols = []
        
        for ensembl_id in ensembl_ids:
            ids.append(ensembl_id)
            if ensembl_id not in self.cache: #not in the cache
                symbol = self.fetch(ensembl_id) #get the symbol
                symbols.append(symbol) #add it to the symbols list
                self.cache[ensembl_id] = symbol #cache the value
            else: #if its in the cache
                symbols.append(self.cache[ensembl_id]) #if its there, use that value
        
        # return a df
        return pd.DataFrame({
            "Ensembl ID": ids,
            "Gene Symbol": symbols
        })
    

    #fetch the symbols WITH extra stuff (ngl, for this one, I'm not gonna worry about the cache rn)
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
        
    #send the data to a file
    def to_file(self, gene_symbols_df, output_filename):
        gene_symbols_df.to_csv(output_filename)
        print(f"Gene symbols saved to {output_filename}")

