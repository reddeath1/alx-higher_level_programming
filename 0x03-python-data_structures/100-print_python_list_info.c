#include "Python.h"
#include <stdlib.h>

/**
 * print_python_list_info - Main function that print information about a
 * python list object
 * @p: A pointer to generic PyObject which is of PyListObject type
 * Return: (Nothing).
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = NULL;
	size_t lens = 0, i = 0;
	const char *type = NULL;

	lens = PyList_Size(p);
	list = (PyListObject *)p;
	printf("[*] Size of the Python List = %ld\n", lens);
	printf("[*] Allocated = %ld\n", (signed long)(list->allocated));
	for  (; i < lens; i++)
	{
		type = Py_TYPE(list->ob_item[i])->tp_name;
		printf("Element %ld: %s\n", i, type);
	}
}
