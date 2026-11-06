# Creating Private Spaces | MuleSoft Documentation

**Source:** [https://docs.mulesoft.com/cloudhub-2/ps-create-configure](https://docs.mulesoft.com/cloudhub-2/ps-create-configure)

---

- 
Select the [region](ps-gather-setup-info#private-network-region)where you want your apps to run.

# Creating Private Spaces

To extend your network to Anypoint Platform, create a *private space*,
a virtual, private, and isolated network hosted in CloudHub 2.0,
to deploy your apps to.

## Create a Private Space

- 
From Anypoint Platform, select **Runtime Manager**>**Private Spaces**.The page shows any private spaces associated with the selected business group. 
- 
Click **Create private space**.
- 
Enter a [name](ps-gather-setup-info#private-space-name)for your private space and click**Create**.You cannot rename your private space after you create it. 

## Create a Private Network

| You can’t change the private network configuration after it’s created.
To change the configuration, delete the private space and create it again.
See [Managing Private Spaces](ps-manage). | 

- 
From Anypoint Platform, select **Runtime Manager**>**Private Spaces**.The page shows any private spaces associated with the selected business group. 
- 
Click the name of the private space to manage. 
- 
On the **Network**tab, click**Create Private Network**.
- 
On the **Create Private Network**page:If you select **Canada (Central)**, subnet count depends on your control plane. Existing MuleSoft Government Cloud private spaces in this region don’t receive three-subnet support automatically. See[Canada (Central) Private Space Subnet Availability](ps-gather-setup-info#ca-central-subnet-availability).

- 
Enter the [CIDR block](ps-gather-setup-info#cidr-block), which is the range of IP addresses that your apps can use.
- 
Optionally, reserve your corporate private network’s CIDRs to connect to your private space by entering them in a comma-separated list. When you reserve your corporate CIDRs, Anypoint Platform creates IPs for your private space without using these blocks to prevent conflicts with your corporate private network. 
- 
Click **Create**.

The private network can take up to 30 minutes to create.

+
While the network is created, you can
[create a connection to an external network](#create-connection-to-external-network).
. After the network creation succeeds, you can [deploy an application](ch2-deploy-private-space) to test the private network connection.

If the private network creation fails, delete it and click **Create Private Network** to try again.

### Resolve Private Domains in Your Internal Network

If your corporate network uses internal DNS servers to resolve requests to custom domains, configure the private space with these IP addresses and domain names. The private space uses your internal DNS to resolve internal host names of your private network (make sure your applications call the backend resources by FQDN).

- 
From Anypoint Platform, select **Runtime Manager**>**Private Spaces**.
- 
Click the name of the private space to manage. 
- 
On the **Network**tab, click the**Configure**link for**Internal DNS servers**.
- 
Enter the (comma-separated) [server IP addresses](ps-gather-setup-info#server-ip-addresses)for your internal DNS servers.
- 
Enter the (comma-separated) [domain addresses](ps-gather-setup-info#domains)to be resolved by internal DNS.
- 
Click **Save**.

After you configure internal DNS, the **Network** tab indicates the number of configured server IP addresses and domains:

![Internal DNS configuration in the Private Network section](_images/internal-dns.png) 

| You can’t add MuleSoft domains or public domains as private space internal DNS. | 

## Create a Connection to an External Network

After you create your private network, connect it to an external network using a VPN or transit gateway attachment.

- 
From Anypoint Platform, select **Runtime Manager**>**Private Spaces**.
- 
Click the name of the private space to manage. 
- 
On the **Network**tab, click**Create Connection**.
- 
On the **Create Connection**page, select the connection type, enter the[VPN](ps-gather-setup-info#vpn-name)or[transit gateway](ps-gather-setup-info#transit-gateway-name)connection name, and click**Next**.Depending on the connection type you selected: - 
**VPN**: Follow the steps in[Creating VPN Connections](ps-create-configure-vpn).
- 
**Transit Gateway**: Follow the steps in[Creating Transit Gateway Attachments](ps-create-configure-tgw).
 
-