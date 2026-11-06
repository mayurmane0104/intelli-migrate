# Step C: Downgrade the node - AWS Elemental Live

**Source:** [https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/downgrades-lv-upg-dg-node.html](https://docs.aws.amazon.com/elemental-live/latest/upgradeguide/downgrades-lv-upg-dg-node.html)

---

When you downgrade AWS Elemental Live , run the installer with the
        `--downgrade` switch for each
      node.

###### To downgrade the node

- 
              From the Linux prompt, log in with the *elemental*user credentials. Once you are logged in, the initial directory is`/home/elemental`.
- 
              Enter the following command. For example: `[elemental@hostname ~]$`**chmod 755 elemental_production_live_2.23.5.12345.run**
- 
              Run the installer with the skip-all option. Use the following commands with the actual file name of the `.run`file, rather than the example below:- 
                  For GPU and CPU versions of the software: `[elemental@hostname ~]$`**sudo sh ./elemental_production_live_2.23.5.12345.run -c --skip-all --start -xeula --downgrade**
- 
                  For CPU-only versions of the software: `[elemental@hostname ~]$`**sudo sh ./elemental_production_live_cpu_2.23.5.12345.run -c --skip-all --start -xeula --downgrade**
 Switches are as follows: - 
                  `2.23.5.12345`: Is the software version that you're downgrading to.
- 
                  `-xeula`: Skips the prompts to read through the EULA. You are prompted once to accept it.
- 
                  `--start`: Specifies to start the services without being prompted.
- 
                  `--downgrade`: Tells the installer that an earlier version is being installed.
- 
                  `--restore-db-backup <path>`: Installs the old version of the database backup file. Provide the path and file name in the following format:`/home/elemental/elemental-db-backup_``<version>`_`<date>`.tarFollowing our example, enter: `/home/elemental/elemental-db-backup_2.23.5_2021-02-08_21-01-36.tar`
 
- 
                  
-  
              Restart the node with the following command: `[elemental@hostname ~]`**sudo reboot**Repeat the downgrade steps on each worker node before moving on to the next step in the downgrade process.