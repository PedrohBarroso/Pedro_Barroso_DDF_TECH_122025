# Etapa 1 - Definir o Dataset

> **Contexto & Decisão:** Pivotei de um dataset complexo (`product-search-corpus`) para um mais estruturado (`Yellow-Taxi`), priorizando a viabilidade dentro do cronograma.

### Relato do Candidato
*   O processo seletivo iniciou com a tentativa de uso do dataset "product-search-corpus", este dataset é uma base de dados sobre  anúncios de diversos produtos, porém organizados de maneira desestruturada ou semi-estruturada. O formato do arquivo é JsonL. 

    O obstáculo observado ao utilizar este dataset foi que devido a natureza desestruturada dos dados, a complexidade para realizar a etapa de ETL séria muito alto, demandaria um tempo extra para estudo, estruturação, organização e definição de uma abordagem que, no meu ponto de vista, é incompatível com o cronograma da entrega.
    
    A minha decisão, foi de pivotar para um dataset mais simples e melhor estruturado, dessa forma, eu escolhi o dataset "Yellow-Taxi-Trip_NY", este dataset é uma base de dados sobre as viagens de táxi realizadas em New York pela linha amarela.
    
    Vale ressaltar que ao insistir em um dataset inviável ou com um custo de transformação maior para o tempo e cronograma proposto, pode-se considerar um erro grave de gestão de projetos.*


### Resumo Técnico
- **Dataset Inicial:** `product-search-corpus` (JSONL)
- **Desafio:** Complexidade de ETL vs Prazo.
- **Dataset Escolhido:** `Yellow-Taxi-Trip_NY` (Parquet).
