---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-public-key-infrastructure-pki/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.hashicorp.com/favicon.svg)

Enterprises leverage [Public key infrastructure (PKI)](https://www.vaultproject.io/use-cases/automated-pki-infrastructure) to encrypt, decrypt, and authenticate information between servers, digital identities, connected devices, and application services. PKI is used to establish secure communications to abate risks to data theft and protect proprietary information as organizations increase their reliance on the internet for critical operations. This post will explore how public key cryptography enables related keys to encrypt and decrypt information and guarantee the integrity of data transfers.

#### PKI and digital identity

Governed by the [International Telecommunications Union (ITU)](https://www.itu.int/rec/T-REC-X.509), which maintains the [X.509 standard](https://www.hashicorp.com/blog/certificate-management-with-vault) that specifies the format of PKI-based certificates, PKI certificates are encountered daily by online users visiting websites, using mobile apps, accessing documents, and working with connected devices. 

PKI-based certificates verify authenticity of many well-known certificates, including:

* SSL/TLS
* Email signing
* Code signing
* Document signing

The core technology that enables PKI is public key cryptography, also known as asymmetric encryption. Asymmetric encryption is used to create a public key, pair it with a private key, and create an association between the two. Plain text is encrypted and converted to ciphertext by an encryption key. Once the data is delivered to the recipient, the decryption key is used to decrypt the ciphertext back to plain text so they can read the original message, confident that it hasn’t been compromised.

![PKI](https://www.datocms-assets.com/2885/1697504081-pki-process.png)Public keys are discoverable. They are published and are not strictly controlled. The private key however, is known only by its owner. Public keys are paired with an associated private key by generating random numeric combinations of variable length, which makes it difficult for hackers to crack them using brute-force attacks.

Here are some of the benefits of asymmetric encryption:

* **Authentication:** Asymmetric encryption helps you to verify identities in a way that no one can fake or contest (known as non-repudiation). This process is ideal for encrypting data between third parties who don’t know each other.
* **Secure key exchanges:** Asymmetric key exchange protocols facilitate symmetric key exchange (more on that below) via public channels that would otherwise be susceptible to [man-in-the-middle (MitM) attacks](https://csrc.nist.gov/glossary/term/man_in_the_middle_attack).
* **Data integrity:** Asymmetric encryption offers assurances that your data hasn’t been altered or modified through the use of digital signatures.

#### Symmetric key algorithms

PKI is asymmetric by definition, but why doesn’t PKI use two private secret keys instead of one private key and one public key? Asymmetric encryption, which uses two separate keys and more complex algorithms in the encryption and decryption process, is slower for encrypting and decrypting large amounts of data.

[Symmetric key](https://www.cryptomathic.com/news-events/blog/symmetric-key-encryption-why-where-and-how-its-used-in-banking) cryptography is the process whereby two private secret keys are generated for encryption and decryption. Symmetric encryption is faster and uses only one key, making it great for large organizations and businesses that need to encrypt vast quantities of data. But while it may appear counterintuitive, symmetric algorithms for PKI are less secure because they require both parties, the sender and receiver, to have access to the private secret keys. 

This means symmetric encryption is typically best suited for non-public channels, such as those inside an organization, while asymmetric encryption is often used for public channels, such as zero trust networks and the public internet. 

#### PKI benefits

The goal of PKI is confidential and secure communications, by allowing two communicating parties to send and receive sensitive data privately. The benefits of PKI to individuals and enterprises include:

* Protecting customers data privacy
* Securing an enterprise’s intellectual property
* Improving technology compliance
* Preventing compromised data
* Securing remote and distributed workloads
* Protecting large numbers of IoT devices

PKI prevents unauthorized use or access by leveraging cryptographic keys as a validation method to protect digital identities and data. It should be a major part of enterprise cybersecurity programs to protect:

* Websites
* E-commerce transactions
* Documents
* Emails
* Servers
* Other digital assets

PKI is a scalable digital identity security solution that secures billions of daily communications. That scalability is enabled by combining widely distributed public keys with secret private keys that are required to decrypt the message. 

#### Common PKI use cases

PKI technology is applied to applied to wide variety of common use cases, including:

* **Web server security:** PKI is the basis for the secure sockets layer (SSL) and transport layer security (TLS) protocols, which underpin HTTPS secure web browser connections.
* **Digital signatures and document signing:** PKI is often used to encrypt messages, but key pairs can be used for digital signatures and document signing by using the sender's private key to verify their digital identity.
* **Code signing:** Engineers use PKI for code signing as a verification method to ensure their code is safe and can be trusted,
* **Email certificates:** S/MIME certificates are used to validate the sender and encrypt the message’s contents to protect users from social engineering and phishing.
* **Secure shell (SSH) keys:** SSH keys are used to authenticate identity and protect services from unintended use or malicious attacks.
* **Digital identity:** The foundation of a [zero trust security strategy](https://www.hashicorp.com/resources/introduction-to-zero-trust-security) is establishing digital identity to authenticate individuals, infrastructure, data, applications, and services.

#### The role of PKI certificate authorities

The certificate authority (CA) is an important element for deploying X.509 PKI certificates. The CA publishes the public key associated with an individual’s private keys. Trusted CAs make it possible to ensure the sender is using the right public key associated with the receiver's private key. Otherwise, malicious actors could compromise the communications being sent.

![PKI](https://www.datocms-assets.com/2885/1698355647-pki-certificate-authority.png)Regardless of the deployment approach, the CA must:

* Verify the identity of all senders’ public keys associated with the CA.
* Ensure public keys are correctly associated with the appropriate private keys.
* Safeguard the organization's data from attacks.

Automating PKI certificate management with HashiCorp Vault

Certificate management may appear to be a mundane task, but manually validating and managing certificates can be time consuming and expensive. Manually provisioning or rotating a certificate for even simple use cases like SSL for a single web server involves multiple steps and can take longer than an hour. 

Extrapolate that to provisioning, renewing, and revoking thousands, or millions, of PKI certificates for an organization’s connected devices, workloads, and identities. Manually managing certificates at scale also introduces significant opportunities for human error that could result in system outages, downtime, and even security breaches, further increasing the costs.

Automating certificate management must be a cornerstone of an enterprise’s PKI strategy. [HashiCorp Vault Enterprise](https://www.hashicorp.com/products/vault/features) and [HCP Vault](https://portal.cloud.hashicorp.com/sign-up?product_intent=vault&ajs_aid=f25a7b06-a96e-4e67-9909-42ce4495e6c7) allow organizations to establish their own trusted CAs and provide a centralized control plane to manage their certificates and safeguard their internal and external communications. Vault Enterprise allows organizations to self manage their PKI and CA environment, while HCP Vault is a SaaS-based PKI option that lets customers focus on PKI management while HashiCorp manages the infrastructure. Both options let customers tap into HashiCorp’s comprehensive support and customer success programs.

By leveraging protocols like [Automated Certificate Management Environment (ACME)](https://www.hashicorp.com/blog/what-is-acme-pki), HashiCorp Vault enables enterprises to achieve an end-to-end automated certificate lifecycle management (CLM) process that includes certificate provisioning, configuration, rotation, revocation, and deployment. Automating PKI certificate management delivers a clear return on investment (ROI) by reducing risk, achieving regulatory compliance goals, reducing operational costs, and shortening time-to-market.

Vault PKI provides:

* **Automation**: Automatically provision, revoke, and rotate PKI certificates based on organizational policies and best practices.
* **Workflow**: Use [protocols](https://developer.hashicorp.com/vault/tutorials/secrets-management/pki-acme-caddy) and [APIs](https://developer.hashicorp.com/vault/api-docs/secret/pki) that can help manage common actions associated with certificate management.
* **Scalability**: Easily scale to thousands or millions of certificates, with high performance clustering.
* **Agility & flexibility**: Manage the underlying architecture yourself with Vault Enterprise or let HashiCorp support your Vault infrastructure with HCP Vault.
* **Visibility**: Vault enables a central control plane to view and manage certificates.
* **Auditability:** Organize and audit certificate events for compliance.

#### Using Vault to meet your PKI needs

The demand for protecting workloads, applications, services, and IoT connected devices is driving rapid growth and demand for PKI services. These environments tend to be highly distributed — geographically as well as technologically — forcing IT teams to cope with multiple PKI automation platforms. 

PKI is a critical pillar in Vault’s [zero trust security](https://www.hashicorp.com/solutions/zero-trust-security) architecture, where everything is authenticated, every action is authorized, and data is always protected.

Vault is a multi-cloud platform that automates and unifies certificate management with a single control plane. It supports automated provisioning, installation, revocation, and renewal of a wide array of X.509 certificates via industry standard PKI protocols, APIs, and more than 200 partner integrations. 

Learn more about Vault PKI through these resources or [get in touch with our team](https://www.hashicorp.com/contact-sales?interest=vault).

* **[What is PKI ACME](https://www.hashicorp.com/blog/what-is-acme-pki)**: Learn about the ACME protocol for PKI, the common problems it solves, and why it should be part of your certificate management roadmap.
* **[PKI hosting options](https://www.hashicorp.com/blog/pki-hosting-cloud-based-pki-vs-self-managed):** Discover the benefits and differences of hosting PKI workloads in the cloud versus an on-premises approach.
* **[X.509 certificate management with Vault](https://www.hashicorp.com/blog/certificate-management-with-vault)**: Practical public key certificate management in HashiCorp Vault using dynamic secrets rotation.
* **[CIEPS availability with Vault 1.15](https://www.hashicorp.com/blog/vault-1-15-brings-ui-updates-pki-enhancements-new-betas-and-more)**: HashiCorp Vault 1.15 contains a range of updates, including PKI enhancements.
