# File generator

The file generator tech test comes with a mock data CSV that represents one of the many types of data that we have to deal with.

The challenge is to consume and transform the CSV file in to a nested JSON file which will form a tree structure.

## Getting Started

Use this repository as a starting point with the CSV file readily available in the root.

### Prerequisites

Use any IDE or resources that you would like. You can attempt this using any technologies you like, make sure you justify your choices.

## The desired form

From the CSV, you will see that the data follows a parent child structure. The first entry is always at the top of the tree, with the following entries being children of the previous column. The example below shows the structure that we would like to see.

```
{
  "label": "Meat & Fish",
  "id": "179549",
  "link": "https://groceries.retailer.com/browse/179549",
  "children": [
    {
      "label": "3 For £9.00 Meat & Poultry",
      "id": "179545",
      "link": "https://groceries.retailer.com/browse/179549/179545",
      "children": []
    },
    {
      "label": "Fish",
      "id": "176741",
      "link": "https://groceries.retailer.com/browse/179549/176741",
      "children": [
        {
          "label": "Fish Counter",
          "id": "176780",
          "link": "https://groceries.retailer.com/browse/179549/176741/176780",
          "children": [
            {
              "label": "Salmon",
              "id": "176979",
              "link": "https://groceries.retailer.com/browse/179549/176741/176780/176979",
              "children": []
            }
          ]
        }
      ]
    }
  ]
}
```
## Tasks
The task is to convert the provided CSV into JSON (see the example for the structure desired).

Remember that we would prefer the beginner task done well rather than all three done poorly. These menus can vary drastically in size and nesting, therefore you should remain aware of that when writing your solution and think about more columns and rows being in other CSV files that may be processed by your solution.

Please separate your tasks into feature branches using git-flow. `feature/beginner feature/intermediate feature/advanced`

### Beginner
Create a simple application that can run locally on a unix environment that has uses some sort of package management tool for your chosen language. There should be a few unit tests testing the main logic of your program.

### Intermediate
Your working solution should be dockerised and be able to be executed as an task on cloud platform. Also contain unit and integration tests.

### Advanced
Given you have completed the first two tasks. A CI/CD pipeline should be created to allow automatic deployment and running of tests. End to end tests should be created to test your solution on your chosen cloud platform. You should aim to have a solution that can be used by a non technical user and supply some interface for them to upload a csv file. 


## Deliverables

Replace the contents of this README.md with:

A covering note explaining the technology choices you have made.

1. Any instructions required to run your solution and tests in a Linux environment.
2. Email as an attachment or a link the git bundled repository showing your commit history with all your commits on the master branch:

```
    git bundle create <anything>.bundle --all
```



""" Feature/Intermediate Task:
GitHub Link:- https://github.com/Chandra314S/cognizant_tech_test_intermediate.git

Step1:- 
-- Creating Docker image using Docker application.
-- A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
-- Using docker build users can create an automated build that executes several command-line instructions in succession.
-- You can specify a repository and tag at which to save the new image if the build succeeds:

Docker command:- "docker build -t  docker_image . "

Step2:- 
-- Install the AWS CLI 
-- Download and run the AWS CLI MSI installer for Windows (64-bit): "https://awscli.amazonaws.com/AWSCLIV2.msi"
-- Alternatively, you can run the msiexec command to run the MSI installer. "msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi".
-- To confirm the installation, open the Start menu, search for cmd to open a command prompt window, 
and at the command prompt use the aws --version command.
-- Retrieve an authentication token and authenticate your Docker client to your registry.
Creating ECR repository in AWS
Use the AWS CLI:
In Local command prompt run below commands to create ECR repository and creating Docker image in AWS cloud.
-- Connecting local repository to AWS ECR:-"aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/x5p7h8v0"

-- Build your Docker image using the following command "docker build -t cognizant_tech_test".
-- After the build completes, tag your image so you can push the image to this repository: 
Docker tag cognizant_tech_test:latest public.ecr.aws/x5p7h8v0/cognizanttechtestintermediate:latest
-- Run the following command to push this image to your newly created AWS repository:
docker push public.ecr.aws/x5p7h8v0/cognizanttechtestintermediate:latest.

Step3:- 

Deploying Docker image from ECR to ECS to deploy web application.
-- ECS cluster is a logical grouping of tasks or services.Your tasks and services are run on infrastructure that is registered to a cluster.
--ECS>>Clusters(create clusters)>>select:- EC2 Linux + Networking click on next step>>Configure cluster>>Create
-- Select launch type compatibility(EC2)>>Configure task and container definitions>>Add Container ECR repository
-- To run task in cluster >>Cluster>>tasks>>Run new task>>Run task.
-- Link for web application:- http://ec2-35-177-134-92.eu-west-2.compute.amazonaws.com:7777/ """.
