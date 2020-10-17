
        set terminal png size 550,400 truecolor font "DejaVuSansMono,9"
        set output "test-ndr.png"
        set style line 1 linecolor rgb "#ff4400"
        set style line 2 linecolor rgb "#0084ff"
        set style increment user
        set grid back lc rgb "#dddddd"
        set xlabel "Alternate allele frequency"
        set ylabel "Non-reference Discordance Rate"
        set y2label "Number of genotypes"
        set xrange [0.0:1.0]
        set y2tics

        plot '-' with lines lw 1 title "NDR", \
             '-' axes x1y2 with lines lw 1 title "GTs"
        end

end
