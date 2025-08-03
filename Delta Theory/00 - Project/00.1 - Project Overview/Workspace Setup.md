---
type: meta
domain:
  - meta
aliases:
  - workspace setup
  - obsidian setup
  - project tools
  - knowledge base environment
---

# Project Workspace Setup — Obsidian Environment

This note defines the **recommended application and setup instructions** for working with the ∆‑Theory Knowledge Base. The goal is to maintain a **lightweight, universal, and easily replicable environment**, ensuring structural clarity without dependency on custom plugins.


## 1. Recommended Application: Obsidian

- The entire Knowledge Base is structured for use in **[Obsidian](https://obsidian.md/)** — a local-first, markdown-based knowledge management tool.
    
- Obsidian provides:
    
    - **Graph-based navigation** of structural links.
        
    - **Folder-driven organization**, mirroring the ontology-propagation structure.
        
    - Full compatibility with **plain markdown files** — ensuring portability.
        
    - No reliance on proprietary formats or cloud lock-in.
        


## 2. Required Setup

- **No special plugins are required.**
    
- The system functions within **Obsidian's default feature set**.
    
- Standard graph view, backlinks, and folder navigation are sufficient for:
    
    - Ontology traversal.
        
    - Cross-layer traceability (Ontology ↔ Spec ↔ Model).
        
    - Structural diagram references via internal embeds (e.g., !\[\[Diagram.png]]).
        


## 3. Folder Structure & Navigation Logic

- Folder structure is **explicitly designed for clarity without automation**.
    
- No reliance on automated templates or plugin-generated indices.
    
- The Knowledge Base is structured to allow:
    
    - Manual traceability via **backlinks and forward-links**.
        
    - Visual graph exploration of difference propagation paths.
        

## 4. Version Control & Collaboration

- The entire Knowledge Base is stored in a **private GitHub repository**.
    
- All content is managed through **Git version control**.
    
- Contributors should:
    
    - Clone the repository locally.
        
    - Work within Obsidian.
        
    - Commit changes and push via standard Git workflows.
        
- Syncing across devices can be achieved through:
    
    - **GitHub as primary remote repository**.
        
    - Local tools (Git clients) or command-line Git for versioning.
        

## Related Notes

|Type|Link|Purpose|
|---|---|---|
|Meta|[[Knowledge Base Architecture]]|Defines note types, traceability rules, and folder structure.|
|Meta|[[Roadmap and Development]]|Outlines development phases and expansion path.|
|Meta|[[About the Project]]|Purpose, origin, and scope of the Knowledge Base.|
