
        set terminal png size 600,400 truecolor font "DejaVuSansMono,9"
        set output "first.vcf.gz-dp.png"
        set ylabel 'Fraction of GTs [%]'
        set y2label 'Number of GTs total'
        set y2tics
        set ytics nomirror
        set xlabel 'Depth'
        set xrange [:20]
        plot , '-' using 1:2 axes x1y2 with lines lt 0 title "GTs total"
end
