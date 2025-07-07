---
{"dg-publish":true,"permalink":"/notes/creating-certificates-using-cert-bot/","tags":["notes"]}
---


## Using Azure Key Vault CSR

Just a summary of : <https://trstringer.com/azure-key-vault-lets-encrypt/>

1. Generate the CSR in Azure Key Vault
	- `keyvault > Certificates > Generate/Import`
	- Set `Type of Certificate Authority` to `Certificate issued by a non-integrated CA`
2. Download the CSR
	- `<Cert Name> > Certificate Operation > Download CSR`
	
- Send the CSR to the CA.
	- `sudo certbot certonly --preferred challenges dns --manual --csr ./cert1.csr`
	- Do as it tells you and make a `txt` record
	- -*Pay attention to the output labelled `Full certificate chain is saved at:`*
- Go back to the `Certificate Operation` pane and `Merge Signed Request` with the **Full Certificate Chain**, probably `003_chain.pem`
