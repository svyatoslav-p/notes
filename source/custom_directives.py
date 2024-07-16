from docutils.parsers.rst import directives
from docutils.parsers.rst.directives import unchanged
from docutils import nodes
from sphinx.util.docutils import SphinxDirective

class MystExampleDirective(SphinxDirective):
    has_content = True
    option_spec = {
        "alt-output": directives.unchanged,
        "highlight": directives.unchanged,
    }

    def run(self):
        """Run the directive."""
        content_str = "\n".join(self.content)
        output_str = self.options.get("alt-output", content_str)
        highlight = self.options.get("highlight", "myst")
        backticks = "```"
        while backticks in content_str:
            backticks += "`"
        content = f"""
{backticks}``{{div}} myst-example

{backticks}`{{div}} myst-example-source
{backticks}{highlight}
{content_str}
{backticks}
{backticks}`
{backticks}`{{div}} myst-example-render

{output_str}
{backticks}`
{backticks}``
"""
        node_ = nodes.Element()
        self.state.nested_parse(content.splitlines(), self.content_offset, node_)
        return node_.children

def setup(app):
    app.add_directive("myst-example", MystExampleDirective)

