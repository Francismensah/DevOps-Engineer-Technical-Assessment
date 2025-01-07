flowchart TD
    subgraph "Development"
        Dev[Developers] --> |Push Code| Git[Git Repository]
        Git --> |Webhook| Jenkins[Jenkins Pipeline]
    end

    subgraph "Security"
        Jenkins --> |Static Analysis| SAST[Security Scanning]
        Jenkins --> |Dependency Check| SCA[Software Composition Analysis]
        Jenkins --> |Container Scan| CS[Container Security]
    end

    subgraph "Build and Test"
        Jenkins --> |Build| Build[Build Services]
        Build --> |Unit Tests| Test[Testing]
        Test --> |Integration Tests| IntTest[Integration Testing]
    end

    subgraph "Artifact Management"
        Build --> |Push Images| Registry[Container Registry]
        Registry --> |Signed Images| ArgoCD[ArgoCD]
    end

    subgraph "GitOps"
        Config[Config Repository] --> |Pull| ArgoCD
        ArgoCD --> |Deploy| K8s[Kubernetes Cluster]
    end

    subgraph "Runtime Security"
        K8s --> |Monitor| Security[Security Monitoring]
        K8s --> |Audit| Audit[Audit Logging]
    end