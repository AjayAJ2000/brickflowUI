import json

from brickflowui.vdom import VNode, diff


def _text_children(count: int, prefix: str = "item") -> list[VNode]:
    return [
        VNode(type="Text", props={"value": f"{prefix}-{index}"})
        for index in range(count)
    ]


def test_vnode_serialization():
    handler_registry = {}
    node = VNode(
        type="button",
        props={"className": "btn"},
        children=[VNode(type="text", props={"value": "Click me"})],
        event_handlers={"click": lambda: print("clicked")}
    )
    
    serialized = node.serialize(handler_registry)
    
    assert serialized["type"] == "button"
    assert serialized["props"]["className"] == "btn"
    assert "click" in serialized["props"]
    assert len(handler_registry) == 1
    assert serialized["children"][0]["type"] == "text"

def test_diff_replace_type():
    handler_registry = {}
    old = VNode(type="div")
    new = VNode(type="span")
    
    patches = diff(old, new, handler_registry)
    
    assert len(patches) == 1
    assert patches[0]["op"] == "replace"
    assert patches[0]["node"]["type"] == "span"

def test_diff_props():
    handler_registry = {}
    old = VNode(type="div", props={"color": "red"})
    new = VNode(type="div", props={"color": "blue", "size": "large"})
    
    patches = diff(old, new, handler_registry)
    
    assert len(patches) == 1
    assert patches[0]["op"] == "update_props"
    assert patches[0]["props"] == {"color": "blue", "size": "large"}

def test_diff_children_insertion():
    handler_registry = {}
    old = VNode(type="div", children=[VNode(type="span")])
    new = VNode(type="div", children=[
        VNode(type="span"),
        VNode(type="b")
    ])
    
    patches = diff(old, new, handler_registry)
    
    # In the current implementation, diffing children is index-based.
    # index 0: span vs span -> no patch
    # index 1: None vs b -> insert patch at path [1]
    assert len(patches) == 1
    assert patches[0]["op"] == "insert"
    assert patches[0]["path"] == [1]
    assert patches[0]["node"]["type"] == "b"

def test_diff_children_removal():
    handler_registry = {}
    old = VNode(type="div", children=[
        VNode(type="span"),
        VNode(type="b")
    ])
    new = VNode(type="div", children=[VNode(type="span")])
    
    patches = diff(old, new, handler_registry)
    
    assert len(patches) == 1
    assert patches[0]["op"] == "remove"
    assert patches[0]["path"] == [1]


def test_diff_removes_surplus_children_from_highest_index_first():
    patches = diff(
        VNode(type="Column", children=_text_children(5)),
        VNode(type="Column", children=_text_children(1)),
        {},
    )

    assert [
        patch["path"] for patch in patches if patch["op"] == "remove"
    ] == [[4], [3], [2], [1]]


def test_diff_removes_all_children_from_highest_index_first():
    patches = diff(
        VNode(type="Column", children=_text_children(5)),
        VNode(type="Column"),
        {},
    )

    assert [
        patch["path"] for patch in patches if patch["op"] == "remove"
    ] == [[4], [3], [2], [1], [0]]


def test_diff_removes_nested_surplus_children_from_highest_index_first():
    patches = diff(
        VNode(
            type="Column",
            children=[VNode(type="Row", children=_text_children(5))],
        ),
        VNode(
            type="Column",
            children=[VNode(type="Row", children=_text_children(1))],
        ),
        {},
    )

    assert [
        patch["path"] for patch in patches if patch["op"] == "remove"
    ] == [[0, 4], [0, 3], [0, 2], [0, 1]]


def test_diff_updates_shared_children_before_descending_removals():
    patches = diff(
        VNode(type="Column", children=_text_children(5, "old")),
        VNode(
            type="Column",
            children=[VNode(type="Text", props={"value": "updated"})],
        ),
        {},
    )

    assert patches[0] == {
        "op": "update_props",
        "path": [0],
        "props": {"value": "updated"},
    }
    assert [
        patch["path"] for patch in patches if patch["op"] == "remove"
    ] == [[4], [3], [2], [1]]


def test_diff_inserts_surplus_children_from_lowest_index_first():
    patches = diff(
        VNode(type="Column", children=_text_children(1)),
        VNode(type="Column", children=_text_children(5)),
        {},
    )

    assert [
        patch["path"] for patch in patches if patch["op"] == "insert"
    ] == [[1], [2], [3], [4]]


def test_diff_removed_prop_sets_null():
    handler_registry = {}
    old = VNode(type="div", props={"title": "hello", "color": "red"})
    new = VNode(type="div", props={"color": "red"})

    patches = diff(old, new, handler_registry)

    assert len(patches) == 1
    assert patches[0]["op"] == "update_props"
    assert patches[0]["props"] == {"title": None}


def test_diff_serializes_vnodes_nested_in_changed_props():
    handler_registry = {}
    old = VNode(
        type="Hero",
        props={"actions": [VNode(type="Button", props={"label": "Export"})]},
    )
    new = VNode(
        type="Hero",
        props={
            "actions": [
                VNode(
                    type="Button",
                    props={"label": "Export"},
                    event_handlers={"click": lambda: None},
                )
            ]
        },
    )

    patches = diff(old, new, handler_registry)

    assert patches[0]["op"] == "update_props"
    assert patches[0]["props"]["actions"][0]["type"] == "Button"
    assert "click" in patches[0]["props"]["actions"][0]["props"]
    assert len(handler_registry) == 1
    json.dumps(patches)
