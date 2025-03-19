This is a bioinformatics practice project of Lauren Bell's. It 
is a very small package that can convert a gene's Ensembl ID to it's
respective symbol via the Biomart API. She might add more functionality 
later. Who knows. 

To install this package, use this command: python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps ensembl_converter   

------------------------------------------------------------------------

I'll add better documentation later, but for now, here are the functions available: 
*all symbols are pulled from the hsapiens_gene_ensembl dataset!*

- fetch(ensembl_ID): takes one string with the ID, returns a single symbol
- fetch_many(ensembl_ids): takes a list of IDs, and returns a dataframe with the ID in one column and the gene symbol in the next
- fetch_with_info(ensembl_ids, additional_data): takes a list of IDs and a list with the extra parameter names as strings, and returns a dataframe formatted similarly to fetch_many(), but with the additional data requested. Defaults to just the ID and symbol tho
- to_file(gene_symbols_dataframe, output_filename): takes the dataframe with the symbols you want to save to a csv and puts it at out_put_filename!

------------------------------------------------------------------------

Tutorials I referenced: 

for making the basic package: https://packaging.python.org/en/latest/tutorials/packaging-projects/

for implementing a better package structure: https://realpython.com/python-modules-packages/

for figuring out pytest: https://docs.pytest.org/en/stable/ , https://www.geeksforgeeks.org/getting-started-with-pytest/
