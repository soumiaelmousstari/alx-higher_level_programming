#include "lists.h"

/**
 * is_palindrome - recursive palind or not
 * @head: head list
 * Return: 0 if it not a palindrome
 * 1 if it is a palindrome
*/
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (palind(head, *head));
}

/**
 * palind - funct to know if is palindrome
 * @head: head list
 * @end: end list
 * Return: 1, 0
*/
int palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
