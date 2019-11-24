# Step 1: Import
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Apply the default seaborn theme, scaling & color pallettte
sns.set()


# You can also customize seaborn theme or use one of six variations of the default theme.
# Which are called deep, muted, pastel, bright, dark, and colorblind.
class ColorPalette:
    """
    Build the Color Palette for the application
    """

    @staticmethod
    def plot_color_palette(palette: str):
        """

        Args:
            palette: string

        Returns:

        """
        figure = sns.palplot(sns.color_palette())
        plt.xlabel("Color Palette:" + palette)
        plt.show(figure)


def main():
    """
    Main function handle testing parameters
    Returns:

    """
    palettes = ['deep', 'muted', 'pastel', 'bright', 'dark', 'colorblind']
    color_palette = ColorPalette()
    for palette in palettes:
        sns.set(palette=palette)
        color_palette.plot_color_palette(palette)


if __name__ == "__main__":
    main()
