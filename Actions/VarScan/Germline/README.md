# Insertions and Deletions in each VCF File

In this task, the number of insertions and deletions are calculated per VCF file.

## 1. Input

* The first vcf is with the tumor purity estimate of 0.4 with MIRACUM Capture Regions named *Miracum_0.4.vcf*.

* The second vcf is with the tumor purity estimate of 0.7 with MIRACUM Capture Regions named *Miracum_0.7.vcf*.

* The third vcf is with the tumor purity estimate of 0.4 with Somatic Truth Capture Regions named *Somatic_0.4.vcf*.

* The fourth vcf is with the tumor purity estimate of 0.7 with Somatic Truth Capture Regions named *Somatic_0.7.vcf*.

## 2. Procedure

* Number of Insertions in VCF File

```
vcf2bed --insertions < example.vcf | wc -l > Output.csv
```

* Number of Deletions in VCF File

```
vcf2bed --deletions < example.vcf | wc -l > Output.csv
```

* Number of snvs in VCF File

```
vcf2bed --snvs < example.vcf | wc -l > Output.csv
```

## 3. Outputs

* There are three output csv files with the count of number of insertions, deletions and snvs.
