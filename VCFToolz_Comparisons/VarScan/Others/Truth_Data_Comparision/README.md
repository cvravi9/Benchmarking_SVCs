# Truth Data Comparision

In this comparision, the Somatic VCF files from the Original Data are compared with the Truth Data. Given below are the details.

## 1. Inputs

* The two input vcf files that carry the original somatic data VCF files.

* The first original vcf file with Tumor Sample Purity of 0.7 is named *First-Somatic.vcf*

* The second original vcf file with the Tumor Sample Purity of 0.4 is named *Second-Somatic.vcf*

* Download the truth data from

```
ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/use_cases/mixtures/UMCUTRECHT_NA12878_NA24385_mixture_10052016/na12878-na24385-somatic-truth.vcf.gz
```

* Rename the downloaded file into *Truth-Somatic.vcf*.

## 2. Procedure

* The Truth-Somatic and the Original Somatic files cannot be compared since the Truth-Somatic doesn't have chr added to the vcf file.

* To add *chr*, the downloaded file should be in vcf format

```
bcftools view -O v Truth-Somatic.vcf.gz > Truth-Somatic.vcf
```

this command will convert the file from vcf.gz to vcf.

* Now the *Chr* can be added by using the command 

```
awk '{if($0 !~ /^#/) print "chr"$0; else if(match($0,/(##contig=<ID=)(.*)/,m)) print m[1]"chr"m[2]; else print $0}' Truth-Somatic.vcf > Updated-Truth-Somatic.vcf
```

* This is the output file that could be used for comparisions and the command is

```
vcftoolz compare Updated-Truth-Somatic First-Somatic.vcf > Output.txt
```

## 3. Outputs

* After the vcftoolz comparision, an output text file along with two pdfs are obtained.

* The first pdf has snps represented in a venn diagram with the file name *venn2.snps.pdf*.

* The second pdf has positions represented in a venn diagram with the file name *venn2.positions.pdf*.
