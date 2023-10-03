
# STREAM PROCESSING TEMPLATE

### Intro

This repo is designed for you to fork and clone locally and onto your EC2 instance.

Make a note of the `.git` url for example:

> `https://github.com/<YOUR_GH_USERNAME>/stream-processing-template.git`

### Terraform Steps

Before running the steps to get into the EC2, head to the [`main.tf`](./main.tf) file and make a note of line 4. You should replace the `<YOUR_GH_USERNAME>` bit of the longer `.git` url to your GitHub username in order to automate the clone of your forked version of this repo as the EC2 instance is being created - *the power of Terraform!*

Once you have reached the step by way of SSH'ing into your EC2 instance, you should have `GIT` installed. You can check by running the command `git --version` in your EC2 shell.


You can then clone your forked version of this repo onto your EC2, and be able to run the Kafka Consumer with `python3 consumer.py`.

If you start seeing some messages with `JSON` data that looks a little like this:

``` json
{"country": "United States", "population": 331073550, "monster_name": "GIANT-VULTURE", "damage": 90000, "updated_population": 330983550, "percent_loss": 0.108, "ts": "2023-10-03 14:53:14.488663"}
```

Then you're on the right track!