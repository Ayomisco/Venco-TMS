This Tenant Management System (TMS) project aims to design and develop a software application to simplify and streamline the management of multi-tenant properties.

Resources
--------
* [Database Schema](https://drive.google.com/file/d/1fAZogBe4lfYjhIbSPLc77gjGKWAj3Xoe/view?usp=share_link)

* [Business Logic](https://drive.google.com/file/d/1IOqzJSJPCYb0xwsJwcpoM9N74XW80KVG/view?usp=share_link)

Features
--------

* User Authentication
* Agent Management## Tenant Management System

A Tenant Management System (TMS) project aims to design and develop a software application to simplify and streamline the management of multi-tenant properties.

Features
--------

* User Authentication
* Agent Management
* Owner
* Tenant
* Rental Agreement
* Billing
* Payment
* Utility Vending and many more...

Requirements
------------

'''Python 3.10+ (v14)
Node.js 16
Redis 6                                       (caching and realtime updates)
MariaDB 10.6.6+ / Postgres v12 to v14         (Database backend)
yarn 1.12+                                    (js dependency manager)
pip 20+                                       (py dependency manager)
wkhtmltopdf (version 0.12.5 with patched qt)  (for pdf generation)
cron                                          (bench's scheduled jobs: automated certificate renewal, scheduled backups)
NGINX                                         (proxying multitenant sites in production)'''














#### License

MIT
* Owner
* Tenant
* Rental Agreement
* Billing
* Payment
* Utility Vending and many more...

Requirements
------------

```
Python 3.10+ (v14)
Node.js 16
Redis 6                                       (caching and realtime updates)
MariaDB 10.6.6+ / Postgres v12 to v14         (Database backend)
yarn 1.12+                                    (js dependency manager)
pip 20+                                       (py dependency manager)
wkhtmltopdf (version 0.12.5 with patched qt)  (for pdf generation)
cron                                          (bench's scheduled jobs: automated certificate renewal, scheduled backups)
NGINX                                         (proxying multitenant sites in production)

```

## Frappe Installation
If you haven't already installed Frappe Framework, install it by following the instructions in the [Frappe documentation.](https://frappe.io/docs/user/en/installation)

## App Installation

* Create a new bench:  In the terminal, navigate to the folder where you have installed Frappe Framework and create a new bench using the following command
    ```
    $ bench init [bench-name]
    ```
* Create a new bench:  In the terminal, navigate to the folder where you have installed Frappe Framework and create a new site using the following command
    ```
    $ bench new-site [sitename]
    ```
* Install the TMS app: Navigate to the bench directory and install the TMS app using the following command
    ```
    $ bench get-app https://github.com/Ayomisco/Venco-TMS.git
    ```

* Install dependencies: Install the necessary dependencies for the TMS app by running the following command
    ```
    $ bench install-app Venco-TMS
    ```

* Migrate the database: Migrate the TMS app's database tables by running the following command
    ```
    $ bench migrate
    ```

* Start the development server: Start the development server by running the following command:
    ```
    $ bench start
    ```

* Set up the app: Access the TMS app through your browser by navigating to http://localhost:8000. Follow the on-screen instructions to set up the app.



##### This guide should provide you with all the steps you need to successfully install the TMS app in a Frappe framework. If you encounter any issues, consult the Frappe documentation or reach out to the TMS app support team for assistance.

