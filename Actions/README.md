# Insertions and Deletions in each VCF File

## Procedure

* Number of Insertions in VCF File

```
vcf2bed --insertions < example.vcf | wc -l
```

* Number of Deletions in VCF File

```
vcf2bed --deletions < example.vcf | wc -l
```
