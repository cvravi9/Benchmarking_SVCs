# Read Depth - vcftools

In this section, Read Depth for the vcf files is visualized using vcftools.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* Getting sequencing depth information

```
vcftools --vcf input.vcf --depth -c > depth_summary.txt
vcftools --vcf input.vcf --site-depth --max-missing 1.0 --out
```

## 3. Outputs

* The first set of outcomes are Miracum_0.4.ldepth, Miracum_0.7.ldepth, Somatic_0.4.ldepth & Somatic_0.7.ldepth.

* The second set of outcomes are Miracum_0.4.log, Miracum_0.7.log, Somatic_0.4.log & Somatic_0.7.log.
