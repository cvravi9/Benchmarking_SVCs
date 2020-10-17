
        set terminal png size 550,400 truecolor font "DejaVuSansMono,9"
        set output "first.vcf.gz-af.png"
        set grid back lc rgb "#dddddd"
        set xlabel "Non-reference allele frequency"
        set ylabel "Concordance"
        set y2label "Number of genotypes"
        set yrange [0.0:1.0]
        set y2tics
        set key center

        plot '-' axes x1y2 with lines lw 1 lc rgb "red" notitle, \
             '-' axes x1y2 with lines lw 1 lc rgb "green" notitle, \
             '-' axes x1y2 with lines lw 1 lc rgb "blue" notitle, \
             '-' with points pt 20 lc rgb "red" title "HomRef", \
             '-' with points pt 20 lc rgb "green" title "Het", \
             '-' with points pt 20 lc rgb "blue" title "HomAlt"
        end
end
end
end
end
end
