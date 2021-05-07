[![Build Status](https://travis-ci.com/csongbird/Pitch-n.svg?branch=main)](https://travis-ci.com/csongbird/Pitch-n)
# Pitch'n

### The Status Quo
Many charities receive items that are unsuitable for their demographic or
are completely unsuable. In terms of clothing donations, many charities 
recieve clothes that are torn, soiled, or otherwise unusable. 25% of clothing 
donations end up in the landfill. Disposing of these items can cost the charity money
and manpower that they cannot afford to spend, rendering the donation moot. 

### Pitch'n's Purpose

Pitch'n is a application that helps both users and charities meet their needs.
Many organizations prefer monetary donations due to the flexibility of its use, 
however, item donations are still a popular method of donation.

Charitable organizations that are looking for certain types of items can connect to the
app and spread the word regarding what they are looking for and the quality that they 
accept. This helps reduce the flow of unusuable and unsuitable items, saving money and effort.

Individual users of the application can see where their donations would be best recieved
and make the greatest impact. 

> Consider Pitch'n to be like a noticeboard, where charities can post their information in
> one place rather than scattered where people may not find it.
 
### Development
To configure your system, first install Python 3 and git. You must have `make` installed. Then run `make dev_env` to set up the environment and install some dependencies using `pip`. 

To run tests on the python code, run `make tests`. As of now, this tests the files in the [source](https://github.com/csongbird/Pitch-n/tree/main/source) folder. 

To produce a webpage for the endpoints module, run `make docs`. 

To run the back end locally:
* Run `./local.sh` to start the server

### Requirements
The server API must be able to allow users to:
* login and logout
* veiw charity information
* save charities to a favorites list
* view favorites list
* delete charities from favorites list

It must allow charity owners to:
* login and logout
* edit information about their charity
* choose to remove their charity from the app

### Design
Most of the requirements should map onto an API endpoint. 

Some questions to consider are:
* how do you separate between individual user accounts and charity organization user accounts?
* how do you verify the charity organization account?

### Github Repo Documents

The current documents in this repository are:
* [Software Project Management Plan (SPMP-001)](https://github.com/csongbird/Pitch-n/blob/main/Project%20Documents/Pitch_n-SPMP-001.pdf)
* [System Requirements Specification (SRS Version 1.2)](https://github.com/csongbird/Pitch-n/blob/main/Project%20Documents/Pitch_n-SRS-Analysis.pdf)


###### _This Project is being completed through the NYU Tandon School of Engineering for the Senior Design class_
