# Read Depth

In this section, Read Depth for the vcf files are filtered and then visualized through two ways.

## 1. Inputs

* The four input vcf files namely Miracum_0.4.vcf, Miracum_0.7.vcf, Somatic_0.4.vcf & Somatic_0.7.vcf.

* The files with 0.4.vcf are with Tumor Sample Purity of 0.4 and the ones with 0.7.vcf are with Tumor Sample Purity of 0.7.

## 2. Procedure

* In the plots, selected columns are filtered and then plotted using mathplotlib.

* In the vcftools, both the depth summary and the site depth sums are obtained using the commands: 

```
vcftools --vcf input.vcf --depth -c > depth_summary.txt
vcftools --vcf input.vcf --site-depth --max-missing 1.0 --out
```

## 3. Outputs

* In the plots, the output files are csv files with the selected columns and the pdfs with mathplotlib plots.

* In the vcftools. the output files are Miracum_DP_0.4.ldepth, Miracum_DP_0.7.ldepth, Somatic_DP_0.4.ldepth, Somatic_DP_0.7.ldepth and Miracum_DP_0.4.log, Miracum_DP_0.7.log, Somatic_DP_0.4.log, Somatic_DP_0.7.log.
