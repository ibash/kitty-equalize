from kittens.tui.handler import result_handler
from kitty.layout.splits import Pair, Splits

# Equalize windows in a split layout. Similar to vim's Ctrl-w > =
def main():
    pass

def equalize(root):
    count = 2
    if isinstance(root.one, Pair):
        count_one = equalize(root.one) + 1
        if root.horizontal == root.one.horizontal:
            count = max(count, count_one)

    if isinstance(root.two, Pair):
        count_two = equalize(root.two) + 1
        if root.horizontal == root.two.horizontal:
            count = max(count, count_two)
    
    root.bias = 1.0 / count
    return count

@result_handler(no_ui=True)
def handle_result(args, result, target_window_id, boss):
    layout = boss.active_tab.current_layout
    if not isinstance(layout, Splits):
        return
    equalize(layout.pairs_root)
    boss.active_tab.relayout()
