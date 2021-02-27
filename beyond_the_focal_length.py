from diffractsim import MonochromaticField, nm, mm, cm

F = MonochromaticField(
    wavelength=488 * nm, extent_x=17. * mm, extent_y=17. * mm, Nx=2000, Ny=2000,power = 0.2
)

F.add_aperture_from_image(
    "./apertures/QWT.png", pad=(5 * mm, 5 * mm), Nx=2800, Ny=2800
)

F.add_lens(f = 50*cm)
F.propagate(100*cm)


rgb = F.get_colors()
F.plot(rgb, xlim=[-8,8], ylim=[-8,8])
