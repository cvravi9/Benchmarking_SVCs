# Allele Frequency - afplots

In this section, Allele Frequency for the vcf files are visualized using afplot tool.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* The visualized allele frequency through afplots are obtained from the input files using the command

```
afplot whole-genome histogram -v my.vcf.gz -l my_label -s my_sample -o mysample.histogram.png
```

## 3. Outputs

* The first set of output allele frequency files are Miracum_0.4.histogram.png, Miracum_0.7.histogram.png, Somatic_0.4.histogram.png, & Somatic_0.7.histogram.png.

* The second set of output allele frequency files are Miracum_0.4.R, Miracum_0.7.R, Somatic_0.4.R, & Somatic_0.7.R.

