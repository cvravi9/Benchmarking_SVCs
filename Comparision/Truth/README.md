The following steps are taken in preparing Somatic Truth data:

1. Download the source file from **"ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/use_cases/mixtures/UMCUTRECHT_NA12878_NA24385_mixture_10052016/na12878-na24385-somatic-truth.vcf.gz"**
2. Rename the file as **First.vcf.gz**
3. Use the command **bcftools view -O v First.vcf.gz > Second.vcf** to convert the file from vcf.gz to vcf.
4. Add "Chr" to this Second.vcf using the command **awk '{if($0 !~ /^#/) print "chr"$0; else if(match($0,/(##contig=<ID=)(.*)/,m)) print m[1]"chr"m[2]; else print $0}' Second.vcf > Third.vcf"**
4. This is the output file that could be used for comparisions.
