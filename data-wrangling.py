import matplotlib.pyplot as plt
import numpy as np

# Define colors to match the HTML infographic's palette
FONT_COLOR = '#0B2D5B'
PALETTE = {
    'blue': '#0B2D5B',
    'orange': '#F35B04',
    'yellow': '#F18F01',
    'lightBlue': '#006E90',
    'darkGray': '#343a40'
}

def wrap_label(text, width):
    """
    Wraps text to a specified width, splitting by words.
    Mimics the JavaScript label wrapping logic.
    """
    if isinstance(text, list): # Already wrapped
        return text
    if len(text) <= width:
        return text
    words = text.split(' ');
    lines = [];
    current_line = '';
    for word in words:
        # Check if adding the next word would exceed the width
        # If current_line is not empty, add a space before the word
        prospective_line = current_line + (' ' if current_line else '') + word;
        if len(prospective_line) > width and current_line != '':
            lines.append(current_line.strip());
            current_line = word;
        else:
            current_line = prospective_line.strip(); # Update current_line without leading/trailing spaces

    if current_line: # Add any remaining text as the last line
        lines.append(current_line);
    
    return lines if len(lines) > 1 else text; # Return list only if actually wrapped, else original string

# --- 1. Economic Decline Chart (Doughnut/Semi-Circle) ---
def create_economic_decline_chart():
    """Generates the India's Share of Global Economy doughnut chart."""
    labels = ['India\'s Share (1700)', 'Rest of World (1700)', 'India\'s Share (1973)', 'Rest of World (1973)']
    data_1700 = [24.4, 75.6]
    data_1973 = [3.1, 96.9]

    # Create a figure with two subplots side by side
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.patch.set_facecolor('#F8F9FA') # Match body background

    # Plot for 1700
    wedges1, texts1, autotexts1 = axes[0].pie(
        data_1700,
        colors=[PALETTE['orange'], '#e9ecef'],
        autopct='%1.1f%%',
        startangle=270, # Start at bottom
        wedgeprops=dict(width=0.3, edgecolor='w'),
        pctdistance=0.85 # Position of the autopct labels
    )
    # Set text colors
    for text in texts1:
        text.set_color(FONT_COLOR)
    for autotext in autotexts1:
        autotext.set_color('white') # Autopct percentage color

    axes[0].set_title('India\'s Share (1700)', color=FONT_COLOR, fontsize=14)
    axes[0].set_aspect('equal') # Equal aspect ratio ensures that pie is drawn as a circle.

    # Plot for 1973
    wedges2, texts2, autotexts2 = axes[1].pie(
        data_1973,
        colors=[PALETTE['blue'], '#e9ecef'],
        autopct='%1.1f%%',
        startangle=270, # Start at bottom
        wedgeprops=dict(width=0.3, edgecolor='w'),
        pctdistance=0.85
    )
    for text in texts2:
        text.set_color(FONT_COLOR)
    for autotext in autotexts2:
        autotext.set_color('white')

    axes[1].set_title('India\'s Share (1973)', color=FONT_COLOR, fontsize=14)
    axes[1].set_aspect('equal')

    # Add a main title for the whole figure
    fig.suptitle('India\'s Share of Global Economy: 1700 vs 1973', color=FONT_COLOR, fontsize=16, weight='bold')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
    plt.savefig('economic_decline_chart.png', transparent=False, dpi=300)
    print("Economic Decline Chart generated as economic_decline_chart.png")
    plt.close(fig)

# --- 2. Massacre Chart (Horizontal Bar Chart) ---
def create_massacre_chart():
    """Generates the State-Sanctioned Massacres horizontal bar chart."""
    massacre_labels = ['Sétif & Guelma (1945)', 'Madagascar (1947)']
    casualties = [45000, 80000]

    # Apply label wrapping
    # Matplotlib's barh can handle list of strings for yticklabels, which wrap_label produces
    wrapped_labels = [wrap_label(label, 16) for label in massacre_labels]

    fig, ax = plt.subplots(figsize=(8, 4))
    fig.patch.set_facecolor('#F8F9FA') # Match body background
    ax.set_facecolor('#F8F9FA')

    # Use numerical positions for bars, then set labels
    y_pos = np.arange(len(wrapped_labels))
    bars = ax.barh(y_pos, casualties, color=[PALETTE['orange'], PALETTE['blue']], height=0.7)

    ax.set_xlabel('Estimated Casualties', color=FONT_COLOR, fontsize=12)
    ax.set_ylabel('') # No y-label as labels are directly set
    ax.set_title('State-Sanctioned Massacres', color=FONT_COLOR, fontsize=14, weight='bold')

    ax.tick_params(axis='x', colors=FONT_COLOR, labelsize=10)
    # Set y-axis ticks and labels
    ax.set_yticks(y_pos)
    ax.set_yticklabels(wrapped_labels, color=FONT_COLOR, fontsize=10)

    # Invert y-axis to have the first label at the top
    ax.invert_yaxis()

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(FONT_COLOR)
    ax.spines['bottom'].set_color(FONT_COLOR)

    # Customize grid
    ax.xaxis.grid(True, linestyle='--', alpha=0.7, color='#e0e0e0')
    ax.yaxis.grid(False)

    plt.tight_layout()
    plt.savefig('massacre_chart.png', transparent=False, dpi=300)
    print("Massacre Chart generated as massacre_chart.png")
    plt.close(fig)

# --- 3. Empire Tactics Chart (Radar Chart) ---
def create_empire_tactics_chart():
    """Generates the Comparative Colonial Suppression Tactics radar chart."""
    labels = ['Military Violence', 'Legal Disenfranchisement', 'Cultural Erasure',
              'Economic Coercion', 'Divide & Rule']
    british_data = [8, 9, 8, 10, 9]
    french_data = [9, 8, 9, 8, 7]

    # Apply label wrapping
    wrapped_labels = [wrap_label(label, 16) for label in labels]

    # Number of variables
    num_vars = len(labels)

    # Compute angle for each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1] # Complete the loop for plotting

    # Extend data for plotting to close the loop
    british_data += british_data[:1]
    french_data += french_data[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#F8F9FA') # Match body background
    ax.set_facecolor('#F8F9FA')

    # Plot data
    ax.plot(angles, british_data, color=PALETTE['orange'], linewidth=2, label='British Empire')
    ax.fill(angles, british_data, color=PALETTE['orange'], alpha=0.2)

    ax.plot(angles, french_data, color=PALETTE['blue'], linewidth=2, label='French Empire')
    ax.fill(angles, french_data, color=PALETTE['blue'], alpha=0.2)

    # Set up ticks and labels
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(wrapped_labels, color=FONT_COLOR, fontsize=12)

    # Set y-axis limits and labels
    ax.set_ylim(0, 10)
    ax.set_yticks(np.arange(0, 11, 2)) # Major ticks every 2 units
    ax.set_yticklabels([], color=FONT_COLOR) # Hide y-axis numerical labels but keep grid

    # Customize grid lines
    ax.grid(True, linestyle='-', alpha=0.7, color='#ddd')
    ax.yaxis.grid(True, color='#ddd', linestyle='--', alpha=0.7) # Radial grid lines

    ax.set_title('Comparative Colonial Suppression Tactics', color=FONT_COLOR, fontsize=16, weight='bold', pad=20)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1), facecolor='#F8F9FA', edgecolor=FONT_COLOR, fontsize=12, labelcolor=FONT_COLOR)


    plt.tight_layout()
    plt.savefig('empire_tactics_chart.png', transparent=False, dpi=300)
    print("Empire Tactics Chart generated as empire_tactics_chart.png")
    plt.close(fig)

# Generate all charts
create_economic_decline_chart()
create_massacre_chart()
create_empire_tactics_chart()
