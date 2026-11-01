# _plugins/rupiah.rb — filter Liquid untuk menulis angka rupiah dengan pemisah
# ribuan gaya Indonesia: {{ page.price | rupiah }} -> 50.000
#
# Jekyll tidak punya filter number_with_delimiter. Menambah method ke
# Jekyll::Filters saja tidak cukup karena modul itu sudah didaftarkan ke
# Liquid saat Jekyll boot (Strainer menganggapnya sudah termasuk), jadi dipakai
# modul baru lalu didaftarkan sendiri.
#
# Build dengan --safe (GitHub Pages resmi) mengabaikan _plugins: Liquid hanya
# meloloskan angka apa adanya, tidak error.
module RupiahFilters
  def rupiah(input)
    n = input.to_i.to_s
    n.reverse.scan(/\d{1,3}/).join('.').reverse
  end
end

Liquid::Template.register_filter(RupiahFilters)
