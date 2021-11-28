
## Monthly Cost Analysis
Complete a month cost analysis of each Azure resource to give an estimate total cost using the table below:

| Azure Resource | Service Tier | Monthly Cost |
| ------------ | ------------ | ------------ |
| *Azure Postgres Database* |  Basic   |   1845.77 INR       |
| *Azure Service Bus*   |    Basic     |     3.75 INR         |
| *Web App*   |    App Service(F1 : Free)     |     0 INR         |
| *Azure Function App*   | App Service (B1 : 1)        |     894.08 INR         |
| *Azure Storage*   | Basic        |     75.05 INR         |
| *SendGrid Plan*   | Essentials        |     1,122.04 INR         |

## Architecture Explanation

### App Service:
>Azure Web Apps is a fast and simple way to create web apps using ASP.NET, Java, Node.js or PHP.It has built-in CI/CD integration and has zero-downtime deployments. Its takes away most of the complexity and lets us concentrate more on the application itself.
### Pros:
- It has built in infrastructure maintenance, scaling.
- high availability with SLA-backed uptime of 99.95 %
- Continuous Deployment (CI / CD) workflow backed up with [AzureRepos, GitHub, BitBucket]
### Cons:
- Provides no control over the infrastructure 

### Azure  Function App:
>Azure Function Apps provides us a event-driven, serverless compute platform with which we can trigger application events and operations without complex orchestration problems. It povides a seamless pipline to link services together at a reasonable price.

### Pros:
- Pay only when invoked.
- Great debugging support
- Can be used as lightweight https service
- Support of multiple languages
### Cons:
- As it is serverless we have no control over the runtime environments.

### Azure Service Bus: 
>Azure Service Bus is a messaging as a service (MaaS) oferiing from Azure that is realiable and supports hybrid integration 

### Pros:
- We can build reliable and elastic cloud apps with messaging
- Provides Protection from spikes in traffic
- Great for Microcervices 
- Works with  existing on-premises systems 
### Cons:
- None
### Azure Database for PostgreSQL:
> A Fully managed, intelligent and scalable PostgreSQL offering from Azure that eradicates most of the complexity of database management and lets us concentrate more on the application development.

### Pros:
- Provides high availability with up to 99.99 percent SLA
- Provides multiple layers of data redundancy
- Provides AI-powered performance optimisation
### Cons:
- No full end-to-end control
- Expensive as it is a managed service
- Migration between major versions of PostgreSQL is not supported
